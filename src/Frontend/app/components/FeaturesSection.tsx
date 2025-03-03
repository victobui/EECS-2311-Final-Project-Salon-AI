'use client';

import { FC, useEffect, useState } from 'react';
import { useInView } from 'react-intersection-observer';

type FeatureCardProps = {
  title: string;
  description: string;
  className?: string;
  icon: React.ReactNode;
  delay?: number;
};

const FeatureCard: FC<FeatureCardProps> = ({ title, description, className = '', icon, delay = 0 }) => {
    const [inViewRef, inView] = useInView({
      triggerOnce: true,
      threshold: 0.2,
    });

    return (
        <div 
          ref={inViewRef}
          className={`rounded-lg p-8 text-white shadow-lg transition-all duration-500 ${
            inView ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-10'
          } ${className}`}
          style={{ transitionDelay: `${delay}ms` }}
        >
          <div className="mb-6 text-white/90 w-14 h-14 rounded-full bg-white/10 flex items-center justify-center">
            {icon}
          </div>
          <h3 className="text-xl md:text-2xl font-semibold mb-4">{title}</h3>
          <p className="text-white/90">{description}</p>
          <div className="mt-6 pt-4 border-t border-white/10">
            <a href="#" className="inline-flex items-center text-sm font-medium text-white group">
              Learn more
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" 
                className="w-4 h-4 ml-2 transition-transform group-hover:translate-x-1">
                <path strokeLinecap="round" strokeLinejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3" />
              </svg>
            </a>
          </div>
        </div>
      );
    };

    



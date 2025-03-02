// Create CTA Section file
import { useInView } from 'react-intersection-observer';
import Link from 'next/link';

export default function CTASection() {
  const [ref, inView] = useInView({
    triggerOnce: true,
    threshold: 0.2,
  });

  return (
    <section className="py-20 relative overflow-hidden">
      {/* Background gradient */}
      <div className="absolute inset-0 bg-gradient-to-r from-[var(--secondary)] to-[var(--secondary-light)] -skew-y-3 origin-top-right transform scale-110"></div>
      
      {/* Decorative elements */}
      <div className="absolute inset-0">
        <div className="absolute top-0 right-0 w-96 h-96 bg-white/5 rounded-full"></div>
        <div className="absolute bottom-0 left-1/4 w-72 h-72 bg-white/5 rounded-full"></div>
        <div className="absolute top-1/2 left-1/3 w-32 h-32 bg-white/5 rounded-full"></div>
      </div>
    </section>
  )
}
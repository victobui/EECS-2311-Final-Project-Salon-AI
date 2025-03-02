// Create CTA Section file
import { useInView } from 'react-intersection-observer';
import Link from 'next/link';

export default function CTASection() {
  const [ref, inView] = useInView({
    triggerOnce: true,
    threshold: 0.2,
  });
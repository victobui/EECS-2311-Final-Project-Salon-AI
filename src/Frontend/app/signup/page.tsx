'use client';

import { useState } from 'react';
import Link from 'next/link';
import FloatingNav from '../components/FloatingNav';
import Footer from '../components/Footer';

export default function SignUpPage() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [userType, setUserType] = useState('salon-owner');
  
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // Basic validation
    if (password !== confirmPassword) {
      alert('Passwords do not match!');
      return;
    }
    
    // Handle signup logic here
    console.log('Signup attempt with:', { name, email, password, userType });
    // In a real app, you would call an API endpoint
  };
  return (
    <div className="min-h-screen flex flex-col"> </div>)
    
    }

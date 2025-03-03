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
    <main className="flex-grow py-16 bg-[var(--gray-bg)]">
        <div className="container-custom">
          <div className="max-w-md mx-auto bg-white p-8 rounded-lg shadow-md">
            <h1 className="text-2xl font-bold text-center mb-6 text-[var(--secondary)]">Create Your SalonAI Account</h1>
            
            <form onSubmit={handleSubmit} className="space-y-4">
              <div>
                <label htmlFor="name" className="block text-sm font-medium text-gray-700 mb-1">
                  Full Name
                </label>
                <input
                  id="name"
                  type="text"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-[var(--primary)] focus:border-transparent"
                  placeholder="Your Name"
                  required
                />
              </div>
    
    }

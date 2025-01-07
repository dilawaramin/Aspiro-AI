"use client";
import { useState } from 'react';
import { Button, ButtonProps } from "@/components/Button";
import React from "react";
import { twMerge } from "tailwind-merge";
import { Orbit } from '@/components/Orbit';
import Login from '@/sections/Login';

export const navItems = [
  {
    name: "Features",
    href: "#features",
  },
  {
    name: "How to Use",
    href: "#How-to-Use",
  },
  {
    name: "Testimonials",
    href: "#testimonials",
  },
];

export const loginItems = [
  {
    buttonVariant: "primary",
    name: "Sign Up",
    href: "#sign-up",
  },
] satisfies {
  name: string;
  href: string;
  buttonVariant: ButtonProps['variant']
}[];

export const Header = () => {
  const [isMobileNavOpen, setIsMovileNavOpen] = useState(false);
  const [showLogin, setShowLogin] = useState(false);
  return (
    <> 
      <header className="border-b border-gray-200/20 relative z-40"> 
      <div className="container">
        <div className="h-18 lg:h-20 flex justify-between items-center">
          <div className="flex gap-4 items-center">
            <div className="size-10 bg-gray-200 bg-[conic-gradient(var(--color-slate-400),var(--color-gray-300),var(--color-blue-300),var(--color-sky-300),var(--color-slate-400)]"></div>
            <div className="font-extrabold text-2xl">Aspiro AI</div>
          </div>
          <div className="h-full hidden lg:block">
            <nav className="h-full">
              {navItems.map(({ name, href}) => (
                <a 
                href={href} 
                key={href} 
                className="h-full px-10 relative font-bold text-xs tracking-widest text-gray-400 uppercase inline-flex items-center before-:content-[''] before:absolute before:bottom-0 before:h-2 before:w-px before:bg-gray-200/20 before:left-0 after-:content-[''] after:absolute after:bottom-0 after:h-2 after:w-px after:bg-gray-200/20 after:right-0 after:hidden last:after:block"
                >
                  {name}
                </a>
              ))}
            </nav>
          </div>
          <div className="hidden lg:flex">
            {loginItems.map(({ buttonVariant, name, href }) => (
              <a href={href} key={name}>
<Button 
  onClick={() => {
    console.log("Button clicked");
    setShowLogin(true);
  }} 
  variant={buttonVariant}
>
  {name}
</Button>              </a>
            ))}
            {showLogin && <Login onClose={() => setShowLogin(false)}/>}
          </div>
          <div className="flex items-center lg:hidden">
            <button className="size-10 rounded-lg border-2 [background:linear-gradient(var(--color-gray-950),var(--color-gray-950))_content-box,conic-gradient(var(--color-slate-400),var(--color-gray-300),var(--color-blue-300),var(--color-sky-300),var(--color-slate-400))_border-box] relative" onClick={() => setIsMovileNavOpen(!isMobileNavOpen)}>
              <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2">
                <div className={twMerge("w-4 h-0.5 bg-gray-100 -translate-y-1 transition durtation-300", isMobileNavOpen && "translate-y-0 rotate-45")}></div>
              </div>
              <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2">
              <div className={twMerge("w-4 h-0.5 bg-gray-100 translate-y-1 transition duration-300", isMobileNavOpen && "translate-y-0 -rotate-45")}></div> 
              </div>
            </button>
          </div>
        </div>
      </div>
    </header>
    {isMobileNavOpen && (
      <div className='fixed top-18 left-0 bottom-0 right-0 bg-gray-950 z-30 overflow-hidden'>
        <div className='absolute-center isolate -z-10'>
          <Orbit/>
        </div>
        <div className="container h-full">
          <nav className='flex flex-col items-center gap-4 py-8 h-full justify-center'>
            {navItems.map(({ name, href }) => (
              <a href={href} key={name} className='text-gray-400 uppercase tracking-widest font-bold text-xs h-10'>{name}</a>
            ))}
            {loginItems.map(({ buttonVariant, name, href}) => (
              <a href={href} key={name} className='w-full max-w-xs'>
              <Button block variant={buttonVariant}>{name}</Button>
              </a>
            ))}
          </nav>
        </div>
      </div>
    )}
    </>
  );
};

export default Header;

import React from "react";
import { X } from "lucide-react";

function Login({ onClose }) {
  return (
    <div className="fixed inset-0 bg-black bg-opacity-30 backdrop-blur-sm flex justify-center items-center">
        <div className="mt-10 flex flex-col gap-5 text-white">
            <button onClick={onClose} className="place-self-end">
            <X size={30} />
            </button>
            <div className="bg-indigo-600 rounded-xl px-20 py-10 flex flex-col gap-6 items-center mx-4 w-full max-w-md">
                <h1 className="text-2xl font-extrabold text-center">
                    AI SaaS Authentication
                </h1>
                <p className="text-lg font-medium text-center">Sign Up For Updates</p>
                <form className="w-full flex flex-col gap-4">
                    <input
                        type="email"
                        placeholder="Enter E-mail"
                        required
                        className="w-full px-4 py-3 text-black border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-400"
                    />
                </form>
                <button className="w-full py-3 font-medium rounded-md bg-black hover:bg-gray-800 text-white">
                    Sign-Up
                </button>
            </div>
        </div>
    </div>
);
}

export default Login;

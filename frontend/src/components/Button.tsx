import { cva } from "class-variance-authority";
import { HTMLAttributes } from "react";

export type ButtonProps = { 
    variant?: 'primary' | 'secondary';
    block?: boolean; 
} & HTMLAttributes<HTMLButtonElement>;

const classes = cva('text-xs tracking-widest uppercase font-bold h-10 px-6 rounded-lg', {
    variants: {
     block: {
        true: 'w-full',
     },
      variant: {
        primary: 'bg-gray-800 text-gray-200',
        secondary: ''
      },
    },
    defaultVariants: {
      variant: "primary",
      block: false,
    },
  });

export const Button = (props: ButtonProps) => {
    const { className = '', children, ...otherProps } = props;
    return <button className={classes({ ...otherProps, className })}>{children}</button>
};
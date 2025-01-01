import { HtmlHTMLAttributes } from "react"
import { twMerge } from "tailwind-merge"

export const Orbit = (props: HtmlHTMLAttributes<HTMLDivElement>) => {
    return (
        <div className={twMerge("size-[500px] border-red-300 rounded-full", props.className)}></div>
    );
}
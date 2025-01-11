import { Button } from "@/components/Button";
import starsBg from "@/assets/stars.png";

export const Hero = () => {
    return (
        <section className="min-h-screen md:h-[800px] flex items-center justify-center overflow-hidden relative [mask-image:linear-gradient(to_bottom,transparent,black_10%,black_90%,transparent)]" 
        style={{
            backgroundImage: `url(${starsBg.src})`, 
          }}
        >
            <div className="absolute inset-0 bg-[radial-gradient(75%_75%_at_center_center,rgb(160,160,160,.2)_15%,rgb(0,36,140,.3)_78%,transparent)]"></div>
            <div className="absolute h-64 w-64 md:h-96 md:w-96 bg-blue-500 rounded-full border border-white/20 top-1/2 left-1/2 
            -translate-x-1/2 -translate-y-1/2 bg-[radial-gradient(50%_50%_at_16.8%_18.3%,white,white,rgb(90,155,255)_37.7%,rgb(20,30,90))] 
            shadow-[-20px_-20px_50px_rgb(220,220,250,.5),-20px_-20px_80px_rgb(180,180,240,.2),0_0_50px_rgb(90,130,200)]"></div>

            <div className="absolute h-[344px] w-[344px] md:h-[580px] md:w-[580px] border border-white opacity-20 rounded-full top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2">
                <div className="absolute h-2 w-2 left-0 bg-white rounded-full top-1/2 -translate-x-1/2 -translate-y-1/2"></div>
                <div className="absolute h-2 w-2 left-1/2 bg-white rounded-full top-0 -translate-x-1/2 -translate-y-1/2"></div>
                <div className="absolute h-5 w-5 left-full border bg-white rounded-full top-1/2 -translate-x-1/2 -translate-y-1/2 inline-flex items-center justify-center">
                    <div className="h-2 w-2 bg-white rounded-full"></div>
                </div>
            </div>
            <div className="absolute h-[444px] w-[444px] md:h-[780px] md:w-[780px] border border-white/20 rounded-full top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 border-dashed"></div>
            <div className="absolute h-[544px] w-[544px] md:h-[980px] md:w-[980px] border border-white opacity-20 rounded-full top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2">
                <div className="absolute h-2 w-2 left-0 bg-white rounded-full top-1/2 -translate-x-1/2 -translate-y-1/2"></div>
                <div className="absolute h-2 w-2 left-full bg-white rounded-full top-1/2 -translate-x-1/2 -translate-y-1/2"></div>
            </div>
            <div className="container relative mt-16">
                <h1 className="text-8xl md:text-[168px] md:leading-none font-semibold tracking-tighter bg-[radial-gradient(100%_100%_at_top_left,white,white,rgb(80,140,210,.8))]
                 text-transparent bg-clip-text text-center">Aspiro AI</h1>
                <p className="text-lg md:text-xl text-white/70 mt-5 text-center max-w-xl mx-auto">Elevate your productivity with Aspiro AI – your smart companion for staying on top of work and achieving more, effortlessly</p>
               
                <div className="flex justify-center mt-5">
                    <a>
                        <Button block variant="primary">Join Now</Button>
                    </a>
                </div>
            </div>
        </section>
    );
  };
  
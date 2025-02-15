import math
from utils import Math
from src.components import switch

class ColorHSV:
    red : int  = 0
    green: int = 0
    blue : int = 0

class ColorRGB:
    red : int  = 0
    green: int = 0
    blue : int = 0

def hsv_to_rgb(h: float, s: float, v: float) -> ColorRGB :
    
    result = ColorRGB()

    i = math.floor(h / 60)
    f = h / 60 - i
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)

    

    res_switch = i % 6

    if(res_switch == 0):
        # (r = v), (g = t), (b = p)
        result.red = v
        result.green = t
        result.blue = p

    elif(res_switch == 1):
        # (r = q), (g = v), (b = p)
        result.red = q
        result.green = v
        result.blue = p
        
    elif(res_switch == 2):
        # (r = p), (g = v), (b = t)
        result.red = p
        result.green = v
        result.blue = t
    
    elif(res_switch == 3):
        # (r = p), (g = q), (b = v)
        result.red = p
        result.green = q
        result.blue = v

    elif(res_switch == 4):
        # (r = t), (g = p), (b = v)
        result.red = t
        result.green = p
        result.blue = v

    elif(res_switch == 5):
        # (r = v), (g = p), (b = q)
        result.red = v
        result.green = p
        result.blue = q
    
    else:
        raise('Internal error: hsv_to_rgb contain a bug!')

       
    return result


def rgb_to_hsv( color : ColorRGB ) -> ColorHSV :
    
    result = ColorHSV()
    
    max = Math.max(color.red, color.green, color.blue)
    min = Math.min(color.red, color.green, color.blue)

    #s = max === 0 ? 0 : d / max
    d : int = max - min
    
    s : int = 0 if max == 0 else d/max

    h : int

    if(max == min ):
        h = 0
    
    elif(max == result.red ):

        
    switch (max) {
        case min:
            h = 0;
            break;
        case r:
            h = g - b + d * (g < b ? 6 : 0);
            h /= 6 * d;
            break;
        case g:
            h = b - r + d * 2;
            h /= 6 * d;
            break;
        case b:
            h = r - g + d * 4;
            h /= 6 * d;
            break;
    }

    return [h * 360, s, max];
}

export function rgbToHex(r: number, g: number, b: number): string {
    // Convert the float values to their hexadecimal counterparts
    const rHex = Math.floor(r * 255)
        .toString(16)
        .padStart(2, "0");
    const gHex = Math.floor(g * 255)
        .toString(16)
        .padStart(2, "0");
    const bHex = Math.floor(b * 255)
        .toString(16)
        .padStart(2, "0");

    // Combine them into a hex color string
    return `${rHex}${gHex}${bHex}`;
}

export function rgbaToHex(r: number, g: number, b: number, a: number): string {
    // Convert the float values to their hexadecimal counterparts
    const rHex = Math.floor(r * 255)
        .toString(16)
        .padStart(2, "0");
    const gHex = Math.floor(g * 255)
        .toString(16)
        .padStart(2, "0");
    const bHex = Math.floor(b * 255)
        .toString(16)
        .padStart(2, "0");
    const aHex = Math.floor(a * 255)
        .toString(16)
        .padStart(2, "0");

    // Combine them into a hex color string
    return `${rHex}${gHex}${bHex}${aHex}`;
}

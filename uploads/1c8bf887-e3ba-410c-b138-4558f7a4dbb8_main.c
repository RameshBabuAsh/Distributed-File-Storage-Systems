#include <stdint.h>
#include "TM4C123GH6PM.h" 

volatile uint32_t b, x, z; 

int main(void) {
    SYSCTL->RCGCGPIO |= (1U << 5); 
    GPIOF->DIR |= (1U << 3);       
    GPIOF->DEN |= (1U << 3);  

    while (1) {
        // First case: if (3 * x > b)
        if (3 * x > b) {
            x = b & 29;
        } else {
            b = x / 4;
        }

        // Second case: if ((3 * x > b) || (z - b < 25))
        if ((3 * x > b) || (z - b < 25)) {
            x = b & 29;
        } else {
            b = x / 4;
        }

        // Third case: if ((3 * x > b) && ((z - b < 25) || (z + 14 > x)))
        if ((3 * x > b) && ((z - b < 25) || (z + 14 > x))) {
            x = b & 29;
        } else {
            b = x / 4;
        }

        GPIOF->DATA ^= (1U << 3); 
    }
}
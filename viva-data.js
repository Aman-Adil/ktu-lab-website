// S6 Lab Reference - Viva Arcade Questions
const vivaQuestions = {
    'CS': {
        flashcards: [
            {
                question: "What is the primary role of a Lexical Analyzer (Scanner)?",
                answer: "It reads the input characters of the source program, groups them into lexemes, and produces a sequence of tokens as output for the syntax analyzer."
            },
            {
                question: "Explain the difference between TCP and UDP.",
                answer: "TCP (Transmission Control Protocol) is connection-oriented, reliable, guarantees packet delivery, and manages congestion. UDP (User Datagram Protocol) is connectionless, faster, but does not guarantee delivery or packet ordering."
            },
            {
                question: "What is an LL(1) parser?",
                answer: "An LL(1) parser is a top-down parser that reads input from Left to right, constructs a Leftmost derivation, and uses 1 lookahead token to make parsing decisions."
            },
            {
                question: "What is socket programming?",
                answer: "Socket programming is a way of connecting two nodes on a network to communicate with each other. One socket (node) listens on a particular port at an IP address, while the other socket reaches out to form a connection."
            },
            {
                question: "What is the difference between compiler and interpreter?",
                answer: "A compiler translates the entire source code into machine code at once before execution, producing an executable file. An interpreter translates and executes the source code line-by-line during runtime."
            },
            {
                question: "What is the purpose of Address Resolution Protocol (ARP)?",
                answer: "ARP is used to map a known dynamic Internet Protocol (IP) address to a permanent physical machine address, known as a Media Access Control (MAC) address, in a local network."
            },
            {
                question: "What is YACC (Yet Another Compiler-Compiler)?",
                answer: "YACC is a utility/parser generator tool that parses an input stream according to a specified grammar (usually LALR(1)) and generates C code representing the syntax analyzer."
            },
            {
                question: "Explain the Sliding Window Protocol.",
                answer: "It is a flow control protocol for data link layer communication where the sender can transmit multiple packets before receiving an acknowledgment, controlled by a window limit, to optimize network utilization."
            }
        ]
    },
    'EC': {
        flashcards: [
            {
                question: "What is the Nyquist sampling theorem?",
                answer: "It states that a continuous-time signal can be completely represented in its samples and recovered back if it is sampled at a rate greater than or equal to twice the maximum frequency component present in the signal (Fs >= 2*Fm)."
            },
            {
                question: "What is the purpose of an operational amplifier (Op-Amp)?",
                answer: "An op-amp is a high-gain, direct-coupled electronic voltage amplifier with differential inputs and a single-ended output, used to perform mathematical operations, filtering, and signal conditioning."
            },
            {
                question: "What is aliasing and how can it be avoided?",
                answer: "Aliasing is the distortion that occurs when a high-frequency component takes the identity of a lower frequency in the sampled signal due to undersampling. It can be avoided by sampling above the Nyquist rate and using an anti-aliasing low-pass filter."
            },
            {
                question: "Explain amplitude modulation (AM).",
                answer: "AM is a modulation technique where the amplitude of a high-frequency carrier wave is varied in accordance with the instantaneous amplitude of the low-frequency modulating (message) signal."
            },
            {
                question: "What is the difference between microprocessors and microcontrollers?",
                answer: "A microprocessor contains only a CPU on the chip and requires external memory (RAM/ROM) and peripherals. A microcontroller integrates the CPU, memory, and I/O ports all on a single IC chip."
            },
            {
                question: "What is the purpose of a PLL (Phase Locked Loop)?",
                answer: "A PLL is a control system that generates an output signal whose phase is related to the phase of an input signal, widely used for frequency synthesis, clock recovery, and FM demodulation."
            }
        ]
    }
};

// Make it available to window context if not already done
if (typeof window !== 'undefined') {
    window.vivaQuestions = vivaQuestions;
}

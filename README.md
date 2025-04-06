# CRT
This program solves the system of congruences and outputs the congruent value mod $m$ ($a$ mod $m$) using the Chinese Remainder Theorem and Euclidean algorithm.

### CRT Principles
$a$ mod $m$ can be rewritten as a system of equivalent modular equations such that:
1. a = $r_1$ (mod $m_1$)
2. a = $r_2$ (mod $m_2$)
3. a = $r_3$ (mod $m_3$)
  ...
4. a = $r_k$ (mod $m_k$)

$m_k$ must all be relatively prime to each other, i.e. $m_1$ and $m_2$ are relatively prime, $m_2$ and $m_3$ are relatively prime, and $m_1$ and $m_3$ are relatively prime, to be able to solve for $a$ using the Chinese Remainder Theorem.

This Youtube video explains how to apply the CRT.
https://www.youtube.com/watch?v=MdePzlQtnCc

### Euclidean Algorithm Principles
The Euclidean algorithm is used to find the GCD of 2 numbers. The idea is to first divide by each other, then take the remainder and divide the divisor from the previous equation with the remainder. Keep doing this until the remainder = 0, where the GCD is the divisor in this last equation.

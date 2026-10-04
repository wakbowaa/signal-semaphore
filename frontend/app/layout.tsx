import type { Metadata } from 'next';
import './tokens.css';
import './globals.css';
export const metadata: Metadata = { title: 'Signal Semaphore', description: 'A validator-governed constrained communication game on GenLayer.' };
export default function RootLayout({ children }: { children: React.ReactNode }) { return <html lang="en"><body>{children}</body></html>; }

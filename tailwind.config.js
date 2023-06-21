import { text } from 'svelte/internal';

/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      colors: {
         "main": "#bf4040",
         "accent": "#7ec47e",
         "secondary": "#4f4f64",
         "background": "#f2efee",
         "text": "#1a1614"
      }
    },
  },
  plugins: [],
}


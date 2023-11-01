import { createGlobalStyle } from "styled-components";

const GlobalStyle = createGlobalStyle`
body {
    /* To prevent ability to vertically scroll whole body a bit when reaching bottom of the page  */
    overflow: hidden;
    margin: 0;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}
html{
    ${"" /* color variables */}
    --main-black: #000;
    --main-white: #FFF;
    ${"" /* font families */}
    --font-primary: 'Inter';
    ${"" /* font sizes */}
    --font-small: 11px;
    --font-mid: 13px;
    --font-big: 15px;
    --font-huge: 22px;
    ${"" /* line heights */}
    --line-height-small: 11px;
    --line-height-mid: 13px;
    --line-height-big: 16px;
}
*{
    font-family: var(--font-primary);
}
button {
    font-family: var(--font-primary);
    border: none;
    cursor: pointer;
}
h1 {
    font-size: var(--font-big);
}
p {
    font-size: var(--font-small)
}
`;

export default GlobalStyle;
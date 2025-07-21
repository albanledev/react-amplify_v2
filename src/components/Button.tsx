"use client";

import { useState } from "react";

const Button = () => {
  const [count, setCount] = useState(0);

  return (
    <button onClick={() => setCount((count) => count + 1)}>
      count is
      <span id="count">{count}</span>
    </button>
  );
};

export default Button;

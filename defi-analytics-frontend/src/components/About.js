import React from 'react';

const About = () => {
  return (
    <div>
      <h1>About the Project</h1>
      <p>
        The DeFi Analytics Platform is designed to help traders and developers analyze decentralized finance protocols.
        It integrates with popular DEXs like Uniswap, Sushiswap, and Pancakeswap to provide real-time data and trading signals.
      </p>
      <p>
        Key features include:
        <ul>
          <li>Real-time trade signal notifications via Telegram.</li>
          <li>Historical data analysis.</li>
          <li>API documentation for developers.</li>
        </ul>
      </p>
      <a href="https://github.com/alexmorettihhhh/deFi-analytics-platform" target="_blank" rel="noopener noreferrer" className="github-link">
        View on GitHub
      </a>
    </div>
  );
};

export default About;
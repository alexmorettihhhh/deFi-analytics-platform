import React, { useEffect, useState } from 'react';
import ReactMarkdown from 'react-markdown';

const Documentation = () => {
  const [markdown, setMarkdown] = useState("");
  const [language, setLanguage] = useState("ru-RU");

  useEffect(() => {
    const loadDocumentation = async () => {
      const cachedData = localStorage.getItem(`api_doc_${language}`);
      if (cachedData) {
        setMarkdown(cachedData);
      } else {
        const url = `https://raw.githubusercontent.com/alexmorettihhhh/deFi-analytics-platform/main/API_DOC.${language}.md`;
        try {
          const response = await fetch(url);
          if (!response.ok) {
            throw new Error("Не удалось загрузить документацию");
          }
          const data = await response.text();
          setMarkdown(data);
          localStorage.setItem(`api_doc_${language}`, data); // Сохраняем в localStorage
        } catch (error) {
          console.error("Ошибка при загрузке документации:", error);
          setMarkdown("Извините, не удалось загрузить документацию.");
        }
      }
    };
    loadDocumentation();
  }, [language]);

  return (
    <div>
      <h1>Документация API</h1>
      <p>Ниже представлена документация по API платформы DeFi Analytics.</p>
      <div>
        <button onClick={() => setLanguage("ru-RU")}>Русский</button>
        <button onClick={() => setLanguage("en-US")}>English</button>
      </div>
      <div className="markdown-content">
        <ReactMarkdown>{markdown}</ReactMarkdown>
      </div>
    </div>
  );
};

export default Documentation;
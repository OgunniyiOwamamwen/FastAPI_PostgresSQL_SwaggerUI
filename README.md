# Revolutionize Your Development with FastAPIs and PostgreSQL!

FastAPIs, the lightning-fast Python web framework, paired with the robustness of PostgreSQL, offer a powerhouse duo for modern development. FastAPI brings the speed and simplicity of asynchronous programming, making your APIs lightning-fast and highly scalable.

With FastAPI, you can build APIs quickly and efficiently, thanks to its intuitive design and automatic interactive documentation generation. Say goodbye to tedious API documentation tasks – FastAPI handles it for you, ensuring your API documentation stays up-to-date effortlessly.

But what's a powerful API without a robust database to back it up? Enter PostgreSQL, the open-source relational database management system trusted by organizations worldwide. PostgreSQL offers reliability, performance, and advanced features, making it the perfect choice for data-driven applications.

Together, FastAPI and PostgreSQL empower you to build applications that can handle immense loads with ease, while maintaining high performance and reliability. Whether you're building a small-scale application or a large-scale enterprise solution, this dynamic duo has got you covered.

# POSTGRESQL QUERY - LFET JOIN

SELECT QT.question_text, CQ.choice_text FROM public.questions QT LEFT JOIN public.choices CQ ON QT.id = CQ.question_id WHERE CQ.is_correct = true;

SELECT id, question_text FROM public.questions;

SELECT id, question_id, choice_text, is_correct FROM public.choices;

# REQUIREMENT

# CREATE-ENVIRONMENT

python3 -m venv env

source env/bin/activate

# PIP

pip install fastapi sqlalchemy psycopg2-binary uvicorn

# RUN THE APPLICATION

uvicorn main:app --reload

browser - url = Generate Swagger-ui

- http://127.0.0.1:8000/docs#/default
- http://127.0.0.1:8000/docs#/default/create_questions_questions_post

# POST

{ "question_text": "What is the best programming language for webAPI?", "choices":

[

{ "choice_text": "FastAPI", "is_correct": true },

{ "choice_text": "dotNET Core", "is_correct": false }

]

}

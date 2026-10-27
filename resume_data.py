# -*- coding: utf-8 -*-
"""Single source of truth for Suthan K's resume content.

Every string here comes from resume_spec.md. Nothing is invented: no numbers,
companies, dates or achievements that are not in the spec.
"""

NAME = "SUTHAN K"

LOCATION = "Trivandrum, Kerala, India"
PHONE = "+91 93843 40144"
EMAIL = "suthanks2000@gmail.com"
EMAIL_URL = "mailto:" + EMAIL

LINKS = [
    ("suthan.vercel.app", "https://suthan.vercel.app"),
    ("github.com/suthanks2000", "https://github.com/suthanks2000"),
    ("linkedin.com/in/suthan-k", "https://www.linkedin.com/in/suthan-k/"),
]

CONTACT_LINES = [
    f"{LOCATION} | {PHONE} | {EMAIL}",
    " | ".join(label for label, _ in LINKS),
]

# --- Skills: one entry per line, keyed by label (content LOCKED, 46 items) ---
SKILL_LINES = {
    "Languages": "JavaScript (ES6+), TypeScript, Python, SQL",
    "Frontend": "React.js, Next.js, Redux Toolkit, HTML5, CSS3, Tailwind CSS",
    "Backend & APIs": "Node.js, Express.js, FastAPI, Flask, REST APIs, GraphQL, WebSockets (SignalR), Microservices",
    "Databases": "PostgreSQL, MySQL, Redis, TimescaleDB, TypeORM, Prisma",
    "Cloud & DevOps": "AWS (Lambda, ECS, API Gateway, S3, RDS, CloudWatch), Azure, Docker, Nginx, GitHub Actions, Cloudflare, Vercel",
    "Security & Testing": "JWT, RBAC (role-based access control), OAuth2, Keycloak, Vitest",
    "Tools & Practices": "Git, Jira, Agile/Scrum, Data Structures & Algorithms",
}

SKILL_ORDER_FULLSTACK = [
    "Languages", "Frontend", "Backend & APIs", "Databases",
    "Cloud & DevOps", "Security & Testing", "Tools & Practices",
]
SKILL_ORDER_BACKEND = [
    "Languages", "Backend & APIs", "Databases", "Cloud & DevOps",
    "Security & Testing", "Frontend", "Tools & Practices",
]
SKILL_ORDER_FRONTEND = [
    "Languages", "Frontend", "Backend & APIs", "Security & Testing",
    "Cloud & DevOps", "Databases", "Tools & Practices",
]

# --- Experience -------------------------------------------------------------
EXPERIENCE = [
    {
        "header": "Software Engineer | Magpii Innovations | Nov 2025 – Present",
        "bullets": [
            "Develop full-stack features for an Industrial IoT and Digital Twin platform and an "
            "AI-powered Education Management Platform, delivered in Agile sprints.",
            "Built .NET microservices with SignalR, handling 10,000+ concurrent events/sec at "
            "sub-100 ms latency.",
            "Built REST APIs with pagination, search and RBAC across 12+ modules of a live "
            "education platform.",
            "Onboard clients by turning requirements into configurations and features; "
            "resolve live production issues.",
        ],
    },
    {
        "header": "Junior Software Developer | Comorins Technologies | Mar 2025 – Oct 2025",
        "bullets": [
            "Cut manual showing coordination and booking conflicts with client self-booking "
            "and optimised scheduling logic.",
            "Improved SEO and load speed with server-rendered Next.js pages for an AI-powered "
            "real estate platform.",
            "Improved client engagement with AI-powered follow-up automation in Python; secured "
            "APIs with JWT/RBAC and shipped to Vercel via GitHub Actions CI/CD.",
        ],
    },
    {
        "header": "Junior Software Developer | Devaxcel Tech Pvt. Ltd. | Sep 2024 – Mar 2025",
        "bullets": [
            "Cut API response time by 25% by optimising GraphQL and REST APIs, and built React, "
            "TypeScript and Redux Toolkit features for a live HealthTech platform.",
            "Managed PostgreSQL migrations, indexing and TypeORM queries; deployed to AWS Lambda "
            "via GitHub Actions.",
            "Built and maintained order-related Node.js microservices in a 28-service backend, "
            "scaled independently.",
        ],
    },
]

# --- Projects (header = bold name | 5 skills, no role) ----------------------
PROJECTS = [
    {
        "name": "Enterprise Industrial IoT & Digital Twin Platform",
        "stack": "React 19, .NET 8/9, ASP.NET Core, SignalR, PostgreSQL",
        "bullets": [
            "Enabled real-time asset monitoring across plants with 7+ ASP.NET Core microservices "
            "and a React 19 cockpit.",
            "Cut multi-hop graph queries by 45% and sped up time-series aggregations 3x by "
            "combining Apache AGE and TimescaleDB in one PostgreSQL data tier.",
            "Cut client deployment time from 3 weeks to 2 days with a metadata-driven UI configured "
            "through JSON schemas; secured with Keycloak and tested with xUnit and Vitest (85%+ coverage).",
        ],
    },
    {
        "name": "AI-Powered Education Management Platform",
        "stack": "React, Next.js, Node.js, PostgreSQL, AWS ECS",
        "bullets": [
            "Delivered features across 12+ modules for schools, colleges and universities, "
            "keeping data consistent across timetables, assignments and quizzes with class-wise "
            "subject integration.",
            "Resolved API and data compatibility issues by migrating from Prisma/MySQL to raw "
            "PostgreSQL queries.",
        ],
    },
    {
        "name": "HealthTech App – Digital Healthcare Platform",
        "stack": "React, Node.js, PostgreSQL, GraphQL, AWS Lambda",
        "bullets": [
            "Processed 10,000+ daily orders on a live platform for medicine purchases and digital "
            "prescriptions, with staged verification.",
            "Automated order processing and delivery-readiness workflows with AWS Lambda, cutting "
            "manual handling.",
        ],
    },
]

EDUCATION = (
    "Bachelor of Engineering (B.E.) | University College of Engineering, Nagercoil | 2019 – 2022"
)

# --- Summaries --------------------------------------------------------------
SUMMARY_MASTER = (
    "Full Stack Software Engineer with 2+ years of experience building client-facing web "
    "applications with React.js, Next.js, JavaScript, TypeScript, Node.js and Python. Cut API "
    "response time by 25% by optimising REST and GraphQL APIs. Hands-on with JWT/RBAC, "
    "PostgreSQL, Dockerised microservices on AWS and Azure, and CI/CD in Agile teams."
)
SUMMARY_BACKEND = (
    "Backend Software Engineer with 2+ years of experience building scalable backend services and "
    "APIs with Node.js, Express.js, TypeScript and Python. Cut API response time by 25% by "
    "optimising REST and GraphQL APIs. Hands-on with JWT/RBAC, PostgreSQL, Dockerised "
    "microservices on AWS and Azure, and CI/CD in Agile teams."
)
SUMMARY_NODE = (
    "Node.js Developer with 2+ years of experience building scalable APIs and backend services "
    "with Node.js, Express.js, JavaScript and TypeScript, plus React.js and Next.js on the front "
    "end. Cut API response time by 25% by optimising REST and GraphQL APIs. Hands-on with JWT/RBAC, "
    "PostgreSQL, Dockerised microservices on AWS and Azure, and CI/CD in Agile teams."
)
SUMMARY_PYTHON = (
    "Python Developer with 2+ years of experience building backend services, APIs and AI-powered "
    "automation with Python, FastAPI and Flask, alongside Node.js and TypeScript. Cut API response "
    "time by 25% by optimising REST and GraphQL APIs. Hands-on with JWT/RBAC, PostgreSQL, "
    "Dockerised microservices on AWS and Azure, and CI/CD in Agile teams."
)
SUMMARY_FRONTEND = (
    "Frontend Software Engineer with 2+ years of experience building responsive, client-facing web "
    "applications with React.js, Next.js, JavaScript and TypeScript. Cut API response time by 25% "
    "by optimising REST and GraphQL APIs. Hands-on with Redux Toolkit, Tailwind CSS, server-side "
    "rendering, JWT/RBAC and CI/CD with GitHub Actions and Vercel in Agile teams."
)
SUMMARY_REACT = (
    "React Developer with 2+ years of experience building responsive, client-facing web "
    "applications with React.js, Next.js, JavaScript and TypeScript. Cut API response time by 25% "
    "by optimising REST and GraphQL APIs. Hands-on with Redux Toolkit, Tailwind CSS, Node.js "
    "APIs, JWT/RBAC and CI/CD in Agile teams."
)

# --- Role versions: only title line, summary and skills order change --------
# key -> (file suffix, title line, summary, skills order)
# The master (Software Engineer) has no file suffix: Suthan_K_Resume.docx/.pdf
ROLES = {
    "software-engineer": (
        "", "SOFTWARE ENGINEER | FULL STACK DEVELOPER",
        SUMMARY_MASTER, SKILL_ORDER_FULLSTACK,
    ),
    "full-stack": (
        "FullStack", "FULL STACK DEVELOPER | SOFTWARE ENGINEER",
        SUMMARY_MASTER, SKILL_ORDER_FULLSTACK,
    ),
    "backend": (
        "Backend", "BACKEND SOFTWARE ENGINEER | FULL STACK DEVELOPER",
        SUMMARY_BACKEND, SKILL_ORDER_BACKEND,
    ),
    "nodejs": (
        "NodeJS", "NODE.JS DEVELOPER | FULL STACK DEVELOPER",
        SUMMARY_NODE, SKILL_ORDER_BACKEND,
    ),
    "python": (
        "Python", "PYTHON DEVELOPER | BACKEND SOFTWARE ENGINEER",
        SUMMARY_PYTHON, SKILL_ORDER_BACKEND,
    ),
    "frontend": (
        "Frontend", "FRONTEND SOFTWARE ENGINEER | REACT DEVELOPER",
        SUMMARY_FRONTEND, SKILL_ORDER_FRONTEND,
    ),
    "react": (
        "React", "REACT DEVELOPER | FRONTEND SOFTWARE ENGINEER",
        SUMMARY_REACT, SKILL_ORDER_FRONTEND,
    ),
}

SECTIONS = ["SUMMARY", "SKILLS", "EXPERIENCE", "PROJECTS", "EDUCATION"]


def skills_for(order):
    """Return [(label, value), ...] in the given order."""
    return [(label, SKILL_LINES[label]) for label in order]

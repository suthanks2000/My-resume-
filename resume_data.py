# -*- coding: utf-8 -*-
"""Single source of truth for Suthan K's resume content.

Every string here comes from resume_spec.md. Nothing is invented: no numbers,
companies, dates or achievements that are not in the spec.
"""

NAME = "SUTHAN K"

CONTACT_LINES = [
    "Trivandrum, Kerala, India | +91 93843 40144 | suthanks2000@gmail.com",
    "suthan.vercel.app | github.com/suthanks2000 | linkedin.com/in/suthan-k",
]

# --- Skills: one entry per line, keyed by label (content LOCKED) -------------
SKILL_LINES = {
    "Languages": "JavaScript (ES6+), TypeScript, Python, SQL",
    "Frontend": "React.js, Next.js, Redux Toolkit, HTML5, CSS3, Tailwind CSS",
    "Backend & APIs": "Node.js, Express.js, FastAPI, Flask, REST APIs, GraphQL, WebSockets, Microservices",
    "Databases": "PostgreSQL, MySQL, MongoDB, TypeORM",
    "Cloud & DevOps": "AWS Lambda, Docker, GitHub Actions, CI/CD, Cloudflare, Vercel",
    "Security & Testing": "JWT, RBAC, OAuth2, Jest, PyTest",
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
# Wording pass done (duty-speak out, one number per bullet, verbs de-duplicated).
# Still open: the owner's real metrics for Magpii and Comorins.
EXPERIENCE = [
    {
        "header": "Software Engineer | Magpii Innovations | Nov 2025 – Present",
        "bullets": [
            "Build client-facing features end to end with React.js, Node.js and Express.js, from "
            "requirement breakdown through to release in cross-functional Agile sprints.",
            "Design and maintain the REST APIs behind those features, including the integration "
            "points with other systems.",
            "Diagnose and resolve production errors across live application workflows, keeping "
            "client-facing features stable.",
            "Onboard new clients by translating their requirements into product configuration and "
            "the features their setup needs.",
        ],
    },
    {
        "header": "Junior Software Developer | Comorins Technologies | Mar 2025 – Oct 2025",
        "bullets": [
            "Built server-side-rendered web applications with Next.js and TypeScript.",
            "Developed Node.js REST APIs and secured them with JWT authentication and role-based "
            "access control (RBAC).",
            "Automated manual steps in internal processes with AI-powered features and application "
            "workflows written in Python.",
            "Maintained the GitHub Actions and Vercel CI/CD pipelines used for application "
            "releases.",
        ],
    },
    {
        "header": "Junior Software Developer | Devaxcel Tech Pvt. Ltd. | Sep 2024 – Mar 2025",
        "bullets": [
            "Optimised REST and GraphQL APIs, cutting API response time by 25%.",
            "Developed React.js features in TypeScript.",
            "Managed PostgreSQL migrations, indexing and secure queries for efficient data "
            "retrieval.",
            "Containerised microservices with Docker, deployed backend functions on AWS Lambda and "
            "supported the CI/CD pipelines and system integration for releases.",
        ],
    },
]

# --- Projects ---------------------------------------------------------------
# Owner's call: no work-vs-personal labels, keep all three. Project dates still open.
PROJECTS = [
    {
        "name": "Enterprise Industrial IoT & Digital Twin Platform",
        "stack": ".NET 8/9, ASP.NET Core, React 19, Azure, Docker",
        "bullets": [
            "Designed and deployed 7+ Docker microservices on Azure Container Apps for telemetry "
            "ingestion, graph models and caching.",
            "Streamed 50,000+ telemetry points/sec at sub-80 ms latency (SignalR WebSockets, Azure "
            "Event Hubs); cut graph query latency 42% with Apache AGE on PostgreSQL.",
            "Delivered a low-code React 19 + Redux Toolkit cockpit that reduced dashboard "
            "configuration deployments by 80%; Azure DevOps GitOps pipelines with Trivy scanning "
            "kept releases under 12 minutes.",
        ],
    },
    {
        "name": "HealthTech Platform",
        "stack": "React.js, TypeScript, Node.js, PostgreSQL, AWS Lambda",
        "bullets": [
            "Built order-management workflows supporting 10,000+ daily orders; automated backend "
            "tasks with AWS Lambda.",
            "Implemented JWT authentication and RBAC, and integrated REST and GraphQL APIs with "
            "microservices.",
        ],
    },
    {
        "name": "Learning Management System",
        "stack": "React.js, Node.js, REST APIs",
        "bullets": [
            "Created responsive learning modules and REST APIs for course management and "
            "dashboards.",
            "Fixed defects and supported deployment and integration alongside QA, UI/UX and "
            "product teams.",
        ],
    },
]

EDUCATION = (
    "Bachelor of Engineering (B.E.) | University College of Engineering, Nagercoil | 2019 – 2022"
)

# --- Summaries --------------------------------------------------------------
SUMMARY_MASTER = (
    "Full Stack Software Engineer with 2+ years of experience building scalable, client-facing web "
    "applications with React.js, Next.js, JavaScript, TypeScript, Node.js and Python. Cut API "
    "response time by 25% by optimising REST and GraphQL APIs. Hands-on with JWT/RBAC "
    "authentication, PostgreSQL indexing, Dockerised microservices on AWS and CI/CD in "
    "cross-functional Agile teams."
)
SUMMARY_BACKEND = (
    "Backend Software Engineer with 2+ years of experience building scalable backend services and "
    "APIs with Node.js, Express.js, TypeScript and Python. Cut API response time by 25% by "
    "optimising REST and GraphQL APIs. Hands-on with JWT/RBAC authentication, PostgreSQL indexing, "
    "Dockerised microservices on AWS and CI/CD in cross-functional Agile teams."
)
SUMMARY_NODE = (
    "Node.js Developer with 2+ years of experience building scalable APIs and backend services "
    "with Node.js, Express.js, JavaScript and TypeScript, plus React.js and Next.js on the front "
    "end. Cut API response time by 25% by optimising REST and GraphQL APIs. Hands-on with JWT/RBAC "
    "authentication, PostgreSQL indexing, Dockerised microservices on AWS and CI/CD in "
    "cross-functional Agile teams."
)
SUMMARY_PYTHON = (
    "Python Developer with 2+ years of experience building scalable backend services, APIs and "
    "AI-powered automation with Python, FastAPI and Flask, alongside Node.js and TypeScript. Cut "
    "API response time by 25% by optimising REST and GraphQL APIs. Hands-on with JWT/RBAC "
    "authentication, PostgreSQL indexing, Dockerised microservices on AWS and CI/CD in "
    "cross-functional Agile teams."
)
SUMMARY_FRONTEND = (
    "Frontend Software Engineer with 2+ years of experience building responsive, client-facing web "
    "applications with React.js, Next.js, JavaScript and TypeScript. Cut API response time by 25% "
    "by optimising REST and GraphQL APIs. Hands-on with Redux Toolkit, Tailwind CSS, server-side "
    "rendering, JWT/RBAC authentication and CI/CD with GitHub Actions and Vercel in "
    "cross-functional Agile teams."
)
SUMMARY_REACT = (
    "React Developer with 2+ years of experience building responsive, scalable, client-facing web "
    "applications with React.js, Next.js, JavaScript and TypeScript. Cut API response time by 25% "
    "by optimising REST and GraphQL APIs. Hands-on with Redux Toolkit, Tailwind CSS, Node.js APIs, "
    "JWT/RBAC authentication and CI/CD in cross-functional Agile teams."
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

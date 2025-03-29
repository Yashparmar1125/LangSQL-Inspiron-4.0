# LangSQL - AI-Powered SQL Assistant

LangSQL is an AI-driven web application that helps developers generate, translate, and optimize SQL queries for multiple SQL engines, including **Trino** and **Spark SQL**. It enables seamless database interactions through natural language processing.

## Features

- **Schema Generator**: Generates optimized database schemas from natural language descriptions.
- **AI Query Builder**: Converts natural language queries into SQL statements for Trino or Spark SQL.
- **Multi-Database Support**: Works with PostgreSQL, MySQL, and other databases configured via Trino.
- **Query Execution & Optimization**: Executes queries through Trino/Spark SQL and provides real-time performance feedback.
- **Adaptive Learning**: Improves query accuracy based on user feedback.
- **User Authentication**: Secure API access through Django DRF and API keys.
- **Dark Mode & Responsive UI**: Optimized for desktop and mobile interfaces.

## Tech Stack

### **Frontend**
- React 18
- TypeScript
- Vite
- TailwindCSS
- Monaco Editor
- React Router
- Framer Motion
- Headless UI
- Lucide Icons

### **Backend**
- **Express.js** (Node.js) -Main Application server Handles Trino/Spark SQL ,MySQL, PostgreSQL interactions.
- **Django REST Framework (DRF)** - Manages AI model Processing ,API authentication, logging, and query history.
- **MongoDB** - Stores user preferences and query logs.
- **AES-256**- Encrypts users data and stores in Database.

### **SQL Execution Engine**
- **Trino** (for distributed query execution)
- **Spark SQL** (for large-scale analytics queries)

## Prerequisites

- **Node.js** 16.x or later
- **npm** 7.x or later
- **Python** 3.9+
- **MongoDB** installed & running
- **Trino/Spark SQL** configured with necessary catalogs

## Getting Started

### **1. Clone the repository**
```bash
   git clone https://github.com/yourusername/langsql.git
   cd langsql
```

### **2. Install dependencies**
```bash
   npm install  # Install frontend dependencies
   cd drf-server && pip install -r requirements.txt  # Install backend dependencies
```

### **3. Start the Backend Services**
```bash
   # Start Django API server
   cd drf-server
   python manage.py runserver
```

```bash
   # Start Express.js API (for Trino/Spark integration)
   cd server
   npm run dev
```

### **4. Start the Frontend**
```bash
   cd client
   npm run dev
```

### **5. Open in Browser**
Navigate to: `http://localhost:5173`

## Trino/Spark SQL Configuration

To use **Trino/Spark SQL**, configure the database connections in **Trino’s catalog** files.

Example MySQL catalog (`etc/catalog/mysql.properties` for Trino):
```ini
connector.name=mysql
tcp-port=3306
connection-url=jdbc:mysql://localhost:3306
table-names=your_table_name
table-types=TABLE
```

You can **query Trino/Spark SQL directly via the LangSQL UI**, without manually configuring databases in the frontend.

## API Routes

### **Frontend to Express API (Trino/Spark)**
| Method | Endpoint               | Description                  |
|--------|------------------------|------------------------------|
| GET    | `/query-engines`       | List available SQL engines  |
| POST   | `/execute-query`       | Execute AI-generated query  |
| POST   | `/optimize-query`      | Optimize query for Trino/Spark |

### **Frontend to Django API (User Authentication & Logs)**
| Method | Endpoint               | Description                  |
|--------|------------------------|------------------------------|
| POST   | `/register`            | User registration           |
| POST   | `/login`               | User authentication         |
| GET    | `/query-history`       | Fetch previous queries      |
| POST   | `/feedback`            | Improve AI query generation |

## Building for Production

To create a production build:
```bash
   npm run build
```

The built files will be in the `dist` directory.

## Development Commands

- `npm run dev` - Start frontend development server
- `npm run build` - Create production build
- `npm run preview` - Preview production build locally
- `npm run lint` - Run ESLint

## Project Structure
```
LangSQL/
├── client/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   │   ├── Home.tsx
│   │   │   ├── SchemaGenerator.tsx
│   │   │   ├── QueryBuilder.tsx
│   │   │   ├── QueryTranslation.tsx
│   │   │   ├── Execution.tsx
│   │   │   └── About.tsx
│   │   ├── App.tsx
│   │   ├── main.tsx
│   │   └── index.css
│   ├── public/
│   ├── index.html
│   ├── package.json
│   ├── tsconfig.json
│   ├── vite.config.ts
│   ├── tailwind.config.js
│   └── postcss.config.js
│
├── backend/
│   ├── django_api/# LangSQL - AI-Powered SQL Assistant

LangSQL is an AI-driven web application that helps developers generate, translate, and optimize SQL queries for multiple SQL engines, including **Trino** and **Spark SQL**. It enables seamless database interactions through natural language processing.

## Features

- **Schema Generator**: Generates optimized database schemas from natural language descriptions.
- **AI Query Builder**: Converts natural language queries into SQL statements for Trino or Spark SQL.
- **Multi-Database Support**: Works with PostgreSQL, MySQL, and other databases configured via Trino.
- **Query Execution & Optimization**: Executes queries through Trino/Spark SQL and provides real-time performance feedback.
- **Adaptive Learning**: Improves query accuracy based on user feedback.
- **User Authentication**: Secure API access through Django DRF and API keys.
- **Dark Mode & Responsive UI**: Optimized for desktop and mobile interfaces.

## Tech Stack

### **Frontend**
- React 18
- TypeScript
- Vite
- TailwindCSS
- Monaco Editor
- React Router
- Framer Motion
- Headless UI
- Lucide Icons

### **Backend**
- **Express.js** (Node.js) - Handles Trino/Spark SQL interactions.
- **Django REST Framework (DRF)** - Manages API authentication, logging, and query history.
- **MongoDB** - Stores user preferences and query logs.

### **SQL Execution Engine**
- **Trino** (for distributed query execution)
- **Spark SQL** (for large-scale analytics queries)

## Prerequisites

- **Node.js** 16.x or later
- **npm** 7.x or later
- **Python** 3.9+
- **MongoDB** installed & running
- **Trino/Spark SQL** configured with necessary catalogs

## Getting Started

### **1. Clone the repository**
```bash
   git clone https://github.com/yourusername/langsql.git
   cd langsql
```

### **2. Install dependencies**
```bash
   npm install  # Install frontend dependencies
   cd backend && pip install -r requirements.txt  # Install backend dependencies
```

### **3. Start the Backend Services**
```bash
   # Start Django API server
   cd backend
   python manage.py runserver
```

```bash
   # Start Express.js API (for Trino/Spark integration)
   cd backend/express
   npm run dev
```

### **4. Start the Frontend**
```bash
   cd frontend
   npm run dev
```

### **5. Open in Browser**
Navigate to: `http://localhost:5173`

## Trino/Spark SQL Configuration

To use **Trino/Spark SQL**, configure the database connections in **Trino’s catalog** files.

Example MySQL catalog (`etc/catalog/mysql.properties` for Trino):
```ini
connector.name=mysql
tcp-port=3306
connection-url=jdbc:mysql://localhost:3306
table-names=your_table_name
table-types=TABLE
```

You can **query Trino/Spark SQL directly via the LangSQL UI**, without manually configuring databases in the frontend.

## API Routes

### **Frontend to Express API (Trino/Spark)**
| Method | Endpoint               | Description                  |
|--------|------------------------|------------------------------|
| GET    | `/query-engines`       | List available SQL engines  |
| POST   | `/execute-query`       | Execute AI-generated query  |
| POST   | `/optimize-query`      | Optimize query for Trino/Spark |

### **Frontend to Django API (User Authentication & Logs)**
| Method | Endpoint               | Description                  |
|--------|------------------------|------------------------------|
| POST   | `/register`            | User registration           |
| POST   | `/login`               | User authentication         |
| GET    | `/query-history`       | Fetch previous queries      |
| POST   | `/feedback`            | Improve AI query generation |

## Building for Production

To create a production build:
```bash
   npm run build
```

The built files will be in the `dist` directory.

## Development Commands

- `npm run dev` - Start frontend development server
- `npm run build` - Create production build
- `npm run preview` - Preview production build locally
- `npm run lint` - Run ESLint

## Project Structure
```
LangSQL/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   │   ├── Home.tsx
│   │   │   ├── SchemaGenerator.tsx
│   │   │   ├── QueryBuilder.tsx
│   │   │   ├── QueryTranslation.tsx
│   │   │   ├── Execution.tsx
│   │   │   └── About.tsx
│   │   ├── App.tsx
│   │   ├── main.tsx
│   │   └── index.css
│   ├── public/
│   ├── index.html
│   ├── package.json
│   ├── tsconfig.json
│   ├── vite.config.ts
│   ├── tailwind.config.js
│   └── postcss.config.js
│
├── backend/
│   ├── django_api/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── serializers.py
│   │   └── settings.py
│   ├── express/
│   │   ├── server.js
│   │   ├── routes.js
│   │   ├── middleware.js
│   │   ├── package.json
│   │   └── .env
│   ├── requirements.txt
│   ├── manage.py
│   ├── db.sqlite3
│   └── .env
│
├── README.md
└── LICENSE
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Trino](https://trino.io/) for distributed SQL execution
- [Apache Spark](https://spark.apache.org/sql/) for big data processing
- [Monaco Editor](https://microsoft.github.io/monaco-editor/) for the code editor
- [TailwindCSS](https://tailwindcss.com/) for styling
- [React Router](https://reactrouter.com/) for routing
- [Framer Motion](https://www.framer.com/motion/) for animations


│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── serializers.py
│   │   └── settings.py
│   ├── express/
│   │   ├── server.js
│   │   ├── routes.js
│   │   ├── middleware.js
│   │   ├── package.json
│   │   └── .env
│   ├── requirements.txt
│   ├── manage.py
│   ├── db.sqlite3
│   └── .env
│
├── README.md
└── LICENSE
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Trino](https://trino.io/) for distributed SQL execution
- [Apache Spark](https://spark.apache.org/sql/) for big data processing
- [Monaco Editor](https://microsoft.github.io/monaco-editor/) for the code editor
- [TailwindCSS](https://tailwindcss.com/) for styling
- [React Router](https://reactrouter.com/) for routing
- [Framer Motion](https://www.framer.com/motion/) for animations


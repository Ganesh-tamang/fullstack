# Full stack


# Local development setup

### Backend setup

Install all these tools from the official guidelines 🛠️:

1. Install `uv` and install python version `3.12`
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
```bash
uv python install 3.12
```
2. Install `postgresql` - database server

After installing run the following commands to get things up and going 😉:

`cd backend`
1. `make install` - install all the required python packages
2. create `.env` file in the project root with necessary configs following `.env.example` file
3. `make collect-static` - using gunicorn in development as well
4. `make migrate` - apply migration
6. `make dev` - start backend development server

Backend is up and running at `http://localhost:8000/`

### Frontend setup

Install all these tools from the official guidelines 🛠️:

1. Install `nvm` and install `node` version `22.8.*`
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
```
```bash
nvm install 22.8
```
```bash
npm install --global yarn
```

After installing run the following commands to the get development server 😉:

`cd frontend`
1. `make fe-install` - install all the require node packages
2. `make fe-dev` - start frontend development server

Frontend development server should be running at `http://localhost:3000/`

# Use the official Node.js image as the base image
FROM node:14

# Set the working directory
WORKDIR /app

# Copy the frontend code into the container
COPY . .

# Install dependencies
RUN npm install

# Build the frontend
RUN npm run build

# Serve the frontend using Vite
CMD ["npm", "run", "dev"]

FROM node:8.9.3

# Make app directory in the container.
RUN #mkdir /app

# Copy whole code to app directory.
COPY ./* /

# Copy package.json app directory.
COPY package.json /
COPY package-lock.json /

# make app directory as the working directory.
WORKDIR /

# Install dependencies.
RUN npm install

# Expose the port
EXPOSE 8080

# Start the process
CMD ["npm", "start"]
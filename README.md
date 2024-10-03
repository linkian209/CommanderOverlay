# Commander Overlay

Commander Overlay is a web application designed to provide an interactive overlay for Commander games. This project is built using Flask and integrates with Discord for user authentication.

## Table of Contents

- [Installation](#installation)
- [Notes](#notes)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/linkian209/CommanderOverlay.git
    cd CommanderOverlay
    ```

2. Create and activate a virtual environment:
    ```sh
    python3 -m venv env
    source env/bin/activate
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a configuration file in the `instance` folder:
    ```sh
    mkdir -p instance
    touch instance/config.json
    ```

    Add your configuration settings in `instance/config.json`. For example:
    ```json
    {
        "SECRET_KEY": "your_secret_key",
        "SQLALCHEMY_DATABASE_URI": "sqlite:///your_database.db"
    }
    ```

5. Set up the database:
    ```sh
    flask db upgrade
    ```

## Notes

- The project uses PostgreSQL as the production database. The PostgreSQL driver (`psycopg2-binary`) is included in the `requirements.txt` file.
- If you encounter any issues with the installation or setup, please refer to the [official documentation](https://www.postgresql.org/docs/) for PostgreSQL.
- For any additional help, feel free to open an issue on the GitHub repository.

## Usage

1. Run the Flask development server:
    ```sh
    python server.py
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000`.

## Features

- **User Authentication**: Login with Discord.
- **Interactive Overlay**: Customizable banners and overlays for Commander games.
- **Responsive Design**: Mobile-friendly interface.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
# Commander Overlay

Commander Overlay is a web application designed to provide an interactive overlay for Commander games. This project is built using Flask and integrates with Discord for user authentication.

## Table of Contents

- [Installation](#installation)
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

4. Set up the database:
    ```sh
    flask db upgrade
    ```

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
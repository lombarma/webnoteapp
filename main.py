from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)  # every change in the code will automatically rerun the code

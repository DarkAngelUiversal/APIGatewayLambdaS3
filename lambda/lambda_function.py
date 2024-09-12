def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html',
        },
        'body': '''
        <html>
            <head>
                <title>I want to work at FiveXL</title>
                <style>
                    * {
                        box-sizing: border-box;
                    }
                    body {
                        font-family: 'Arial', sans-serif;
                        margin: 0;
                        padding: 0;
                        background-color: #f9f9f9;
                        color: #333;
                    }
                    header {
                        background-color: #4CAF50;
                        color: white;
                        padding: 20px;
                        text-align: center;
                    }
                    nav {
                        background-color: #333;
                        padding: 10px;
                        display: flex;
                        justify-content: center;
                    }
                    nav a {
                        color: white;
                        padding: 14px 20px;
                        text-decoration: none;
                        text-align: center;
                    }
                    nav a:hover {
                        background-color: #ddd;
                        color: black;
                    }
                    .container {
                        width: 80%;
                        margin: 0 auto;
                        padding: 20px;
                    }
                    section {
                        background-color: white;
                        padding: 20px;
                        margin-bottom: 20px;
                        border-radius: 10px;
                        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                    }
                    footer {
                        background-color: #333;
                        color: white;
                        text-align: center;
                        padding: 10px 0;
                        position: relative;
                        bottom: 0;
                        width: 100%;
                    }
                    /* About section */
                    .about {
                        display: flex;
                        justify-content: space-between;
                    }
                    .about img {
                        max-width: 50%;
                        border-radius: 10px;
                    }
                    /* Contact Form */
                    .contact-form {
                        display: flex;
                        flex-direction: column;
                    }
                    .contact-form input, .contact-form textarea {
                        padding: 10px;
                        margin-bottom: 10px;
                        border: 1px solid #ccc;
                        border-radius: 5px;
                    }
                    .contact-form button {
                        background-color: #4CAF50;
                        color: white;
                        padding: 10px;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                    }
                    .contact-form button:hover {
                        background-color: #45a049;
                    }
                    @media (max-width: 768px) {
                        .about {
                            flex-direction: column;
                            text-align: center;
                        }
                        .about img {
                            max-width: 100%;
                        }
                    }
                </style>

            </head>
            <body>
                <header>
                    <h1>I want to work at FiveXL</h1>
                    <p>I want to work at FiveXL</p>
                </header>


                <div class="container">
                    <section>
                        <h2>Hello, World!</h2>
                        <p>This page is generated using AWS Lambda and API Gateway. It is completely serverless and built to scale automatically with demand.</p>
                        <p>The website is hosted entirely on AWS, making it secure, scalable, and cost-efficient.</p>
                    </section>
                </div>
                <footer>
                    <p>&copy; 2024 My Lambda Website. All rights reserved.</p>
                </footer>
            </body>
        </html>
        '''
    }

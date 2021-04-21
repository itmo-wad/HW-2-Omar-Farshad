
# Assignment 2

<H2>Basic part</H2><BR>

Create web application, which can host your image gallery:

1.1. Listen on localhost:5022

1.2. Render HTML document on http://localhost:5022/

1.3. Show static images on http://localhost:5022/files/images/<image_name>

1.4. Your external CSS and JS files should be returned on http://localhost:5022/files/<js/css filename>


You are allowed to use any JS or CSS frameworks
You are allowed to use only Python programming language and Flask framework <BR>
<H2>Optimal part</H2>
Create web application, which emulates a chat with a human:

1.1. Web page with messages log

1.2. Input for writing new message

1.3. Button for sending message to the server

1.4. Sample HTML form:

     <form method="POST" action="<http://localhost:5000/>">
         <textarea name="messages"></textarea>
         <input type="text" name="new_message">
         <input type="submit">
     </form>
After the button click message should be sent to the server with HTTP POST to http://localhost:5022/:

2.1. It is okay to send also all messages if you don’t know how to keep them on the server.

2.2. It is also okay to keep them in the global variable

Robot should answer on a message according to the predefined set of rules

3.1. Rules can be hardcoded as bases on the occurencies of different words

3.2. There should be at least 10 rules describing typical conversation topics:

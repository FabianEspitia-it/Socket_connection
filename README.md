# Algorithmic Sciences

- [✅]  Write a server script that binds a port and responds to connections (an unlimited amount of concurrent
connections).
- [✅] Receives "String" in the connection in clear text.
- [✅] the path to find the file comes from the configuration file. The configuration file can have a large number of elements that are not relevant to your server script. The line with the path in it will start with “linuxpath=” and will have the path after it, for example “linuxpath=/root/200k.txt”.
- [✅] Opens the file found in the path, and searches for a full match of the string in the file. Please note: partial matches of the search query string in a line do not count as matches. You should only respond with STRING EXISTS if you can find a match for the whole string as a stand-alone line in the file.
- [✅] REREAD_ON_QUERY option: When set to True, this checks whether "String" exists in the file,
considering that the file in the path COULD change every few microseconds. In this case the code should
re-read the contents of the file on every search query sent from the client. When the option is set to False, the file is not expected to change and it’s enough to read it one time, on load.
- [✅] The maximum payload size is 1024 bytes. The server strips any \x00 characters from the end of the payload it receives.
- [✅] Responds on the TCP port saying "STRING EXISTS" or "STRING NOT FOUND" (with a newline
character at the end).
- [✅] Uses multithreading to accept a large amount of requests in parallel.
- The script will work on linux and needs to work with files up to 250,000 rows, with an average of 40
millisecond execution time per file in case REREAD_ON_QUERY is TRUE, and 0.5 ms if it’s FALSE.
- [✅] On the TCP output, also show the “logs” including the search query, the requesting IP, the measured
execution time, timestamps etc., marked as “DEBUG: “.
- You are allowed to use native Linux scripts to execute the task (wrapped in python), core python, or any libraries. Since speed is a critical part of the specification, do some research and write a small, few-page, well-formatted report in human readable format on the speeds of the different options benchmarked against each other. Your speed report should cover at least 5 different file-search options and algorithms as you have tried, with the performance of each one, with an extra bonus point available for every file-search option beyond 5. Your report should have a table that shows all the algorithms you have tested each other sorted based on performance, and at least one chart that compares all the performances of the algorithms against each other as a function of the number of lines in the file. Your final submission should have the code implemented with the fastest option. You should deliver the report in a PDF format.
- The code needs to run as a linux daemon or service, with clear installation instructions on how to run it as such.
- [✅] The code needs to be protected from attackers. Please handle your buffer overflows and other potential
security issues, and implement SSL authentication between the server and the client, using either a
self-signed certificate or PSK as the authentication method. Make the SSL authentication configurable and
easy to turn off from the configuration file (True/False).
- [✅] The code needs to be PEP8 and PEP20 compliant, statically typed, docstring'd and documented on delivery, neatly and professionally packaged. Remember: you’re here to demonstrate your level of attention to detail and your diligence. So if you’re going to use a tool that promises to simply process your code and make it PEP8 compliant, then beware: if it does not work perfectly, then you’re going to get penalized for submitting non-PEP8-compliant code, and in addition to that, you’re also going to make the wrong impression on your evaluators, which is going to impact the offer you get. Please always check your PEP8 compliance manually, and do it with the eye of a perfectionist, instead of trusting third party tools to do a good enough job for you.
- [✅] Robust exception handling and error messages are required, covered with Unit tests for:
[✅] A. Showing different execution times for different file sizes from 10,000 to 1,000,000 with a client
you write for testing purposes and cover these in your speed testing report,
B. Showing different execution times for file sizes vs. number of queries per second, up to the point
that the server can not handle it anymore (document the limitations of the software),
C. Demonstrating correct workflow in all paths and cases,
D.[✅] Unit testing all exceptions and edge cases is required (use pytest!)
- [✅] Submit your repository to us in email in a zip file when it’s done, complete with tests, speed report,
client.py, and everything else, ready to deploy. Make sure you have everything in there, and make sure you
check the Evaluation Sheet below to score yourself and see that you are making a passing submission.
Also, please make sure not to include any absolute paths in the tests and other places of the repository
because you will get penalized for submitting a repo with unit tests that fail. Make the package stand alone,
and complete, including all test data in the tests directory, and name your files and tests in a way that pytest
can collect them properly and run them fast. Also don’t forget to include a requirements.txt and everything
else that would normally be required for a professional submission.

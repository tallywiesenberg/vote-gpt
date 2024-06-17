What is this project?

Why is the value of the project to prospective users?


## Inspiration
In 73% of voting-age U.S. citizens were registered to vote for presidential elections in 2020, according to the U.S. Census Bureau. [Current Population Survey's November 2020 Voting and Registration Supplement] Not only is this percentage of people registered to vote a 20-year high, according to the Bureau, but so is the number of voting-eligble people who voted in the 2020 elections. A voting-elgible person is defined by the Bureau as a person who is at least 18 years old and U.S. citizen who was either born in the United States or its territories or naturalized. 

However, it is one thing to be registered to vote. It is another to vote. 

According to the Bureau, there was a 73-67

## What it does
Our app works in three phases. The first phase is to collect information directly from the user about the kind of information that is pertinent to their voting needs. We collect the information by  
## Who the prospective users are

## How we built it
Our app has two components: a back end and a front end. 

Back End:
First, we decided to take a functional, nested approach to code organization. The reason for this technical decision was that we needed to process an input without storing any data -- which is why chose to make our code organization functional -- and we implemented nested functions to make the process readable for future contributors.

Then we made the technical decision to use GPT3.5 as our large language model (LLM). Our app requires a LLM to summarize and format unstructured scraped website data into actionable information to send to users. The reason behind this technical decision based on GPT3.5's reliability and neutral tone, as well as it's ability to organize and summarize messy text.

Next, we a built search engine results fetcher to retrieve unstructured text from top results. We experimented with Tavily and Google. However we decided to proceed with Tavily because is designed to work with large language models (LLM) like GPT3.5.  

We also iteratively improved output of meaningful responses by utilizing search engines and prompt engineering. To increase the precision and accuracy of the responses, we restricted search results to `.gov` and `.org` websites. 

...implemented google sheets API to read new data from the google form frontend

tested with pytest

Front End:
First, we contemplated how and where to host the front end of our app. Initially, we were going to host our interface on Flask because it would be able to accept a simple input, such as a user's location. We were planning on only querying a user's location and then providing them a list of tips and resources for voting in their area. However, we realized that we wanted to make the user a passive participant in the app. For that reason, we decided on a form where users could check off the specific voting topics and needs they would like additional information on. In the end, we decided in using a Google Form as a front end because it allows the user to check off of a list. Moreover, Google Forms allows the developers (or app owners) to document and study any kinds of trends in the voting information that users are requesting. 

## Challenges we ran into
One challenge we faced was that none of the APIs we found offered both search engine features and text processing. First, we started with GPT2 but GPT2 required too much tuning. Even with trial and error, we could not resolve this issue. Then, we used GPT3.5 to create search prompts from questions. However, problems with tuning still persisted. 

We observed that replying on GPT to create prompts was the root cause of our challenge. In response, we decided to use the questions themselves as prompts, which simplified the main script and helped us overcome the tuning issue.
 
## Accomplishments that we're proud of
One accomplishment we are proud of is having used prompt enginneering 

## What we learned
From this experience, we learned how valuable human-centered design is for designing educational and public service technology tools. 

## What's next for VoteGPT
There are a few next steps we would implement for VoteGPT. One is training our app to provide responses in plain English. Some of the responses provided by our app -- such as the one regarding legal protections voters have at the polls -- were filled with governmental jargon and had a more formal feel to it. Governmental jargon is not well understood by laypeople, and its exclusivity could become a deterrent for users to use the information provided to them by our app. Because we want our app to be actionable for people from varying career, educational and socio-economic backgrounds it is imperative that we iterate our app to provide responses that are easy to read and understand. 

Another next step would be to send the app output as a text message or email to users' phones. Due to time restraints of the hackathon, the output is currently sent and stored on a Google Sheet. However, because the point of the app is to empower people with the information that can remove barriers to voting, the app needs to be able to send information directly to users. Not everyone uses email or has consistent access to a compter, so that is why we want to make it possible for users to access the information directly on their phone. 
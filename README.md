# VOTEGPT APP


## Inspiration
In 2020, 67% of voting-eligible people voted in the presidential elections, according to the U.S. Census Bureau. [Current Population Survey's November 2020 Voting and Registration Supplement] 
A voting-elgible person is defined by the Bureau as a person who is at least 18 years old and U.S. citizen who was either born in the United States or its territories or naturalized. 

The percentage reported for 2020 voting turnout is a five-percent increase from 2016, when 62% of the voting-eligble population voted in the presidential elections. While 5% might seem like a small increase, the impact of this increase can be better visualized when understood as a quantity of people: 17 million more people voted in 2020 than in 2016. 

And that is with a pandemic. 

We are inspired by this major increase in voters, and want to continue to increase voter turnout in the 2024 election. However, in order to help increase turnout, we must also address reasons why individuals do not vote. 

With our app, VoteGPT, we are addressing socio-economic obstacles individuals may face when trying to vote, such as finding childcare or being able to take time off work in order to vote.

## Who the potential users are
We designed this app to provide actionable information to those who face obstacles to voting. Specific obstacles include not being able to vote due to being unable to access childcare and not being able to get leave from work to vote. 

## What it does
Our app works in three phases. The first phase is to collect information directly from the user about the kind of information that is pertinent to their voting needs. We collect the information through a google form that asks only two questions. Then   

## How we built it
Our app has two components: a back end and a front end. 

Back End:
First, we decided to take a functional, nested approach to code organization. The reason for this technical decision was that we needed to process an input without storing any data -- which is why chose to make our code organization functional -- and we implemented nested functions to make the process readable for future contributors.

Then we made the technical decision to use GPT3.5 as our large language model (LLM). Our app requires a LLM to summarize and format unstructured scraped website data into actionable information to send to users. The reason behind this technical decision based on GPT3.5's reliability and neutral tone, as well as it's ability to organize and summarize messy text.

Next, we a built search engine results fetcher to retrieve unstructured text from top results. We experimented with Tavily and Google. However we decided to proceed with Tavily because is designed to work with large language models (LLM) like GPT3.5.  

We also iteratively improved output of meaningful responses by utilizing search engines and prompt engineering. To increase the precision and accuracy of the responses, we restricted search results to `.gov` and `.org` websites. 

Finally, we tested with pytest.

Front End:
First, we contemplated how and where to host the front end of our app. Initially, we were going to host our interface on Flask because it would be able to accept a simple input, such as a user's location. We were planning on only querying a user's location and then providing them a list of tips and resources for voting in their area. However, we realized that we wanted to make the user a passive participant in the app. For that reason, we decided on a form where users could check off the specific voting topics and needs they would like additional information on. In the end, we decided in using a Google Form as a front end because it allows the user to check off of a list. Moreover, Google Forms allows the developers (or app owners) to document and study any kinds of trends in the voting information that users are requesting. 

Then, to input the specific concerns or obstacles into our LLM, we implemented the google sheets API to read new data from the google form frontend into our backend. 


## Challenges we ran into
One challenge we faced was that none of the APIs we found offered both search engine features and text processing. First, we started with GPT2 but GPT2 required too much tuning. Even with trial and error, we could not receive useful or coherent outputs. We decided to use GPT3.5 as our LLM because its outputs are organized, reliable, and coherent. 

We first used GPT3.5 to both create the search engine prompt from the user's google form data and to summarize the search engine results. However, GPT3.5's search engine prompts were off-target or unspecific, particularly when using Google search.

To get better search results, we replaced Google search with Tavily search, which is a search engine designed to be used in tandem with LLMs. Tavily can also accept questions as search queries, so we no longer needed GPT3.5 to convert the user questions into generic search queries. We decided to use the questions themselves as prompts, which simplified the main script and increased the accuracy and clarity of the final responses.
 
## Accomplishments that we're proud of
One accomplishment we are proud of is having leveraged prompt enginneering to get precise answers from messy, unorganized inputs. We consider this an accomplishment because precise answers will help provide our users action steps to overcoming obstacles they face in casting their ballot. 

## What we learned
From this experience, we learned how valuable human-centered design is for designing educational and public service technology tools. 

## What's next for VoteGPT
There are a few next steps we would implement for VoteGPT. One is training our app to provide responses in plain English. Some of the responses provided by our app -- such as the one regarding legal protections voters have at the polls -- were filled with governmental jargon and had a more formal feel to it. Governmental jargon is not well understood by laypeople, and its exclusivity could become a deterrent for users to use the information provided to them by our app. Because we want our app to be actionable for people from varying career, educational and socio-economic backgrounds it is imperative that we iterate our app to provide responses that are easy to read and understand. 

Another next step would be to send the app output as a text message or email to users' phones. Due to time restraints of the hackathon, the output is currently sent and displayed on the terminal. However, because the point of the app is to empower people with the information that can remove barriers to voting, the app needs to be able to send information directly to users. Not everyone uses email or has consistent access to a compter, so that is why we want to make it possible for users to access the information directly on their phone. 

## How to run locally
First, create `.env` file with relevant enviroment variables for Tavily and OpenAI APIs.

Then, run the following commands:
'''bash
python3 -m venv venv
source venv/bin/activate
python3 -m src.vote_gpt.main
'''
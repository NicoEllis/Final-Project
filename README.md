# Final Project

## 🏁 Final Project

---

The final project is the culminating experience of this course. It’s not unlike what you will experience when you successfully summit a mountain.

It’s your opportunity to take the new skills you have learnt for a stretch, create your own program and show case what you can do to the world!

As long as your project uses knowledge from the lessons, you are free to come up with your own program that it is relevant to digital arts & media.

We highly recommend you create something that is interesting to you, solves a real problem, generates an art work or an interactive game. 

Aim to build something that will have utility and impact beyond this course. 

*e.g. An aesthetically beautiful artwork, an engaging game or a tool that will be useful for other media & arts practitioners and students.*

## Requirements

---

### 📝 Proposal

Creating a project of your own can seem daunting. But let’s apply the principles of dividing and conquering to solve this problem. 

You will write a project proposal following the below requirements & guidelines:

1. **GitHub Repo** - Create a public GitHub Repository. 
    1. Set your repository’s visibility to public and not private.
    2. If you need help creating a GitHub repository, check out GitHub’s [Create A Repo](https://docs.github.com/en/get-started/quickstart/create-a-repo) 
2. **Proposal File** - Create a `proposal.md` file. 
    - Your proposal will be written in the simple markdown syntax. If you are unfamiliar with it, check out the vey helpful GitHub’s [Basic Writing and Formatting Syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).
    - Example `proposal.md` Project Proposal file. You may use the template below.
        
        `proposal.md`
        
        ```markdown
        # Title
        
        ## Repository
        <Link to your project's public GitHub respository>
        
        ## Description
        1-2 sentence description of what it will do and how it relevant to media and digital arts.
        
        ## Features
        - Feature 1
        	- Short explaination of how it will be executed.
        - Feature 2
        	- Short explaination of how it will be executed.
        - Feature N 
        	- Short explaination of how it will be executed.
        
        ## Challenges
        - Short sentence of any skill or topic that needs to be learnt or researched.
        - Short sentence of any skill or topic that needs to be learnt or researched.
        - Short sentence of any skill or topic that needs to be learnt or researched.
        
        ## Outcomes
        Ideal Outcome:
        - Briefly describe what is the ideal outcome?
        
        Minimal Viable Outcome:
        - Briefly describe the bare essential for a good working outcome?
        
        ## Milestones
        
        - Week 1
          1. Goal 1
          2. Goal 2
        
        - Week 2
          1. Goal 1
          2. Goal 2
        
        - Week N (Final)
          1. Goal 1
          2. Goal 2
        ```
        
3. **Title** - State the title of your project.
4. **Repository** - Include a link to your new public GitHub repository. 
    1. It would be pretty empty at the moment. But feel free to include a `README.md` file or even this `proposal.md` if you like.
5. **Description** - 1-2 sentence description of what it will do. If you are solving a problem, briefly tell us why it is relevant to digital arts & media. (e.g. what problem does it solve or what sort of art does it create?)
6. **Features** - List down what features it will have and how do you plan/guess to the feature will be executed?
7. **Challenges** - List down any new skills or topics you will need to learn or research?
8. **Outcomes** - Software projects are infamously hard to predict effort. It’s actually common that one might accomplish less than hoped for. List down in 2-3 short sentences the below outcomes:
    1. **Ideal Outcome** - What is the ideal outcome you hope for this project?
    2. **Minimal Viable Outcome** - What is the minimum viable outcome of this project that still works & demonstrates it’s usefulness or artistic/entertainment value? 
    In other words, if the project turns out more challenging than anticipated, what are the bare essentials you consider as a good outcome?
9. **Milestones** - Guess your weekly goals as milestones to keep you on track. List only 1 to 3 goals a major milestone goals a week.

### 👩‍💻 Design & Implementation

The design and implementation of your program is up to you, but subject to these requirements.

1. **Python** - Your program must be written in Python.
2. **Complexity/Scope** - Your project must take more time and effort to implement than is required from each of the chapter lab sets. 
3. **Functions/Methods** - You must have a `main` function and 3 or more additional functions or class methods in a file called `project.py`
    - Place `project.py` within the `src` folder of the repository.
    - You may implement additional classes and functions beyond the minimum requirement.
    - Examples `project.py` structures
        
        ```python
        def main():
            ...
        
        def function_1():
            ...
        
        def function_2():
            ...
        
        def function_n():
            ...
        
        if __name__ == "__main__":
            main()
        ```
        
        ```python
        def main():
            ...
        
        class SomeClass():
        
            def method_1():
                ...
        
            def method_2():
                ...
        
            def method_n():
                ...
        
        if __name__ == "__main__":
            main()
        ```
        
4. **3rd Party Libraries** - Any `pip`-installable 3rd party libraries that your project requires must be listed in a file called `requirements.txt` in the root of your project. 
    - Libraries must be stated one per line.
    - Place `requirements.txt` at the root of the repository.
    - Example `requirements.txt` file.
        
        ```python
        pygame
        pillow
        ```
        

### 📤 Deliverables

1. **Commentary Demonstration Video** - Create a short (<3 mins) narrated commentary video that demonstrates & presents your project to the world!
    1. **(If needed) Watch the below video on how to record your screen.**
        1. [How to use OBS for Screen Recording or Streaming - Beginner Tutorial](https://youtu.be/ySENWFIkL7c?si=Sdv_2UUNNi0CQFh7). (26 min)
        2. OBS is the recommended tool for screen-recordings.
        3. If you choose to record in  `.mkv`, you may remux it to  `.mp4` h.264 codec with OBS or [HandBrake](https://handbrake.fr/).
    2. **Presentation** -  In addition to screen recordings of demonstrations of how your program works, you may use slides, screenshots, voice overs and even live-action videos
        1. Briefly state the title of your project, your name, and a short description of what you program is about, you may include other details you’ll like to tell the viewer.
        2. Proceed to demonstrate your program working.
        3. State your feature, then say a few words about it and ensure it is shown functioning in the video. Do this one feature at a time.
        4. You may also demonstrate any other features you are most proud of that you would like to highlight about your project.
        5. Watch your video before submitting.
    3. **Be Concise** - Keep your video **<3 mins**. Videos that go over with no good reason, risk being penalized.
    4. **Format** - **MP4** (h.264 codec), minimum **1920x1080** pixels, **24 FPS** or more, **<100mb**
        1. Filename: `pfda_finalProject_<LastnameFirstname>.mp4`
    5. **Upload** - Upload your video to YouTube or equivalent video hosting platform.
        1. Take note of it’s URL, you’ll need it in your `README.md` text file. 
        2. You can set the video as “unlisted” but do not set it as “private”.
2. **README.md file** - Create a `README.md` text file that explains your project.
    - It must include your project title, the URL of your video, URL to your GitHub repository as well as a description of your project.
        - It should be written in the simple Markdown syntax. Once again, if you are unfamiliar with it, check out the vey helpful GitHub’s [Basic Writing and Formatting Syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).
        - Place the `README.md` file in the root folder of your project repository.
        - Example `README.md` file. You may use the template below.
            
            ```markdown
            # PROJECT TITLE
            
            ## Demo
            Demo Video: <URL>
            
            ## GitHub Repository
            GitHub Repo: <URL>
            
            ## Description
            ```
            
    - Your readme file should be a few paragraphs in length and explain what your project is, what do the different files you included in your repository contain or does, any design considerations, future areas of improvements, etc. It’s your written explanation of your project, so take pride in it.

## 💯 Grading Criteria

---

**Project Proposal (5% Overall Course Grade)**

- **20%** - File, Markdown Format and Submission
- **20%** - Title & Description
- **15%** - GitHub Repository
- **15%** - Features
- **10%** - Challenges
- **10%** - Outcomes
- **10%** - Milestones

**Final Project (25% Overall Course Grade)**

- **10% - Deliverables, Files, Formats, Submission** -
    - All files and deliverables were created and submitted correctly. Adhering to file naming conventions, formats, requirements and were submitted to the right platforms.
    - `README.md` text file sufficiently explains the project.
- **20% - Demonstration Video** - Video adheres to all requirements and uploaded to YouTube or similar video hosting platform.
- **30% - Complexity/Scope** - Project is suitably complex in scope and effort.
- **10% - Relevance** - Project is relevant to the field of digital arts & media.
- **20% - Creativity** - Project is either visually creative or exhibits creative problem-solving.
- **10% - Challenge** - New skills and/or topics were learnt, researched and implemented in the project.

## 🎏 Before You Begin

---

1. In VS Code, **Open** the your repository folder.
2. **Run** `cd src` in the terminal to change directories into the `src` folder. This is where you will save your code (a.k.a. source files).
3. If needed, **Execute** `code project.py` to create an empty file called `project.py` . 
4. Implement your code in `project.py` .

## 💾 How to Commit Your Progress?

---

As the saying goes, “commit often and commit early.” 

Examples of stages you should commit is whenever you: 

- pass a test,
- make some tangible progress you’ll regret losing suddenly,
- code up a new feature,
- fixed a bug,
- started a new file with minimal code, etcetera.

These all make great opportunities to commit your changes.
In this course, you are expected to **break up your work into several commits** to show progression.

We want to see how your code evolved and progressed by glancing at your commit history, so ensure you use short but meaningful commit messages. 

**You will be penalized if your commit messages are too generic.** For example:

- “Update 1”, “test”, “committed”, etc.

Looking for tips on how to write better commit messages? Check out:

[How to Write Better Git Commit Messages – A Step-By-Step Guide (freecodecamp.org)](https://www.freecodecamp.org/news/how-to-write-better-git-commit-messages/)

## 📤 How to Submit?

---

**For the proposal, you will:**

1. **Submit the `proposal.md`** onto eLearning before the due date.

*Do not forget to also create an empty Public GitHub Repository and include a link to it in your proposal.*

**For the final project, you will:**

1. **Commit and push** your code as well as any other required files to your public **GitHub** repository.
    1. `src/project.py`
    2. `requirements.txt` 
    3. `README.md`
2. **Upload** your video demonstration on **YouTube**
3. **Submit** your video demonstration of your program on **eLearning.**
4. **Submit** your `README.md` text file on **eLearning**.

---

Whenever you push changes to the GitHub repository on the cloud, your work is submitted.

To ensure your final changes are on GitHub, please review the files in your GitHub repository as well as the autograde test results (if any) after you push your changes from VS Code to GitHub.

You can double-check your submission by going to the “code” section of your GitHub repository, clicking on the `src` folder, and viewing the contents.

**Don’t forget to submit your video demo and `README.md` on eLearning!**
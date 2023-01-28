# Methods

## Deciding what intervention components to focus on

Consulting the list of ideas from my focus groups, I identified which could be implemented by members of the UK EQUATOR Center and presented this subset to them for consideration.

The BCW book suggests prioritizing possible interventions according to their expected Affordability, Practicability, Efficacy, Acceptability, Side-Effects, and Equity (referred to as the APEASE criteria).

Individuals gave each idea a score out of 5 for each criteria, and I then totalled the scores. The ideas that came out on top were the ones that could be implemented by:

* Web-based intervention:
  * Improving the EQUATOR website
  * Extending the website to disseminate reporting guidance
* Providing training
* Providing support services
* Creating a network of "reporting champions", akin to the UK Reproducibility Network.

Interestingly, the team gave low scores to ideas centring around restriction - encouraging journals, funders, or ethics committees to enforce RG adherence - principally because of concerns that such rules would not be acceptable to researchers, would be expensive, and would not be equitable, as RGs adherence would disproportionately burden international or early career researchers, or disciplines where the guidance is less mature or harder to apply. This marked a reversal of opinion from before we started, when most members of EQUATOR were confident that enforcement was the only solution.

Of the prioritized options, improving and extending the EQUATOR website was seen as potentially very effective, very acceptable, affordable, practicable, have no side-effects, and would increase equity. Given the constraints of my PhD, developing training, networks, or a service felt unfeasible.

## Designing intervention components

I went through the list of ideas and pulled out the ones that could be implemented in a web-based intervention. I linked each component with the barrier it was addressing (and the behavioural driver underlying that barrier), the intervention function(s) it was employing, and the idea that inspired it. I described how the component could be realised, and contrasted it to the existing system. See table #TODO for a list of components.

## Building the web-based intervention

Building was iterative and collaborative. I wanted to include EQUATOR UK in the process because I expected them to have insights, but also because I wanted them to understand decisions and to take ownership of it.

We started off by sketching ideas on paper and drafting text in documents. I would visualise these in mockups which helped bring the ideas to life for discussion. Everyone would give feedback, I could create a new iteration and, once happy, I created an alpha version of the pages. These were real web pages in that they could be viewed in a browser and clicked on, but had dummy content to visualize where text and imagery would go. After another round of feedback I refined the alpha version and populated it with real text and images.

Our intention was to populate the guidance pages with a sample of the most frequently accessed guidelines. But because we wanted to manipulate the guidance text, it made sense to start with one reporting guideline and I selected SRQR (see #TODO for my justification). I got written permission from Bridget O'Brien, the lead developer or SRQR, and from the publisher. I kept Bridget up to date with my work and invited her feedback.

Many of the intervention components (#TODO: which one?) required structuring and standardising the content of reporting guideline items. I did this by pasting the SRQR guidance in a text editor and then:

* Rearranging content into categories: what to write, how/where to write it, what to write if the item wasn't/couldn't be done, why the item is important and to whom, examples.
* I re-wrote sentences to speak directly to authors. E.g. "Describe X" instead of "Authors should describe X", and to use active voice. This shortened the text and also made it clearer who the primary audience is. (We included instruction to editors and reviewers so they know they can use the guidance too).  
* I deleted any repetition between the subtitle (which is generally used in the checklist) and the text.
* For composite items I split the sub-items into bulleted lists. E.g.
    > For each X, describe:
    >
    > * X
    > * Y
    > * Z
    >
* I rearranged conditional sub-items so that they read "If X, then describe Y", rather than "Describe Y if X".
* I moved definitions into the glossary.
* I moved contextual notes into footnotes.
* I also removed references for now. They can be re-added should the web-based intervention be made public.
* I edited the resulting text to "join it back together".
* I edited the tone of voice

This process revealed gaps in item description. Most commonly, there was often no guidance of what to write if an item wasn't or couldn't be done. For instance, the target sample size item had no instruction of what to write if you didn't ever have a target in mind. Some items were missing any kind of justification of why the item was important and to whom.

After development, I double checked the intervention against the initial list of intervention components to ensure I had covered all of them.

## System architecture

When considering architecture options for the web-based intervention I prioritized technology that was easily maintainable by EQUATOR staff or a future PhD student. I looked for tools that would be familiar to early career researchers. I considered DIY website builders (like Wix or Squarespace) but these services can be expensive. Most offer a 'drag and drop' building experience which, although easy to use, is a labouriously repetitive way of uploading and formatting large amounts of content. Should EQUATOR want to change how an item is presented, they would have to manually edit each and every item for each and every reporting guideline. Additionally, our intervention components required some custom functionality that wasn't offered by these services (e.g. integration with a DOI minting service, glossary definitions, discussion boards).

Although coding languages like `html` or `javascript` are used by many web developers to create websites, they aren't commonly used in research. Ultimately I decided on `markdown`, an incredible simple language that can be used by anybody who knows how to use Microsoft Word. Markdown is a plain text language. It uses asterixes, underscores, and carets to make text **\*\*bold\*\***, _\_italic\__, or ^\^superscript\^^.#TODO check superscript. Headings, URLS, and references are similarly easy, and can be simplifed further by using one of many readily available editors that make writing markdown feel like writing a Microsoft Word document.

I then use Quarto to turn markdown into html (the website). Quarto, like RStudio, is commonly used by academics to write reproducible manuscripts. It requires no technical knowledge, is easy to learn, has great documentation, and is open source. All files are hosted on Github, a version control repository that is commonly used to house code and data. The website is served using Github Pages which is free and configurable.

The new web-intervention is stored in a Github repository that EQUATOR can access. Each reporting guideline has its own repository, which means that guideline developers can be in control of their own content. When a developer makes a change, these changes are automatically version controlled and "pulled in" to EQUATOR's repository before "going live". This means that EQUATOR has ultimate control over the site, but guideline developers can easily edit their own content.

## Introduction

The output of my focus groups was a long list of ideas. This list included ideas from all stakeholders, including myself, and fed into step 7 of Michie et al.'s guide to applying the Behaviour Change Wheel @michieBehaviourChangeWheel2014. In chapter (see {{< var chapters.workshops >}}) I explained why I expanded on this step. In this chapter I describe my process in more detail by explaining how I used behavioural analysis to identify behaviour change techniques. I then describe how I turned ideas into intervention components and developed these components into an intervention prototype. By intervention component, I mean a designed element that uses one or more behaviour change technique, which is theorized to work through one or more intervention functions to target one or more behavioural drivers. An intervention _change_ is the addition or removal of an element. Defining intervention content in this way is useful because it helps intervention developers to understand why the component has been added (or removed), how it is theorised to be working and, therefore, how its effectiveness may be tested.

## Behavioural Analysis

#### Methods

For every idea generated from the workshops and focus groups, I labelled which barriers it was addressing, which behavioural drivers it was targeting, and which intervention functions it was employing to do so. This list was data driven, in that it was based upon the ideas and barriers generated from previous research (see chapters {{< var chapters.synthesis >}}, {{< var chapters.review >}}, {{< var chapters.web-audit >}}, {{< var chapters.journal-audit >}}, {{< var chapters.workshops >}} and {{< var chapters.focus-groups >}}). To give structure and context to this list, I grouped ideas according to the sub-behaviours they targeted: 1) engaging with guidance and 2) applying it (see section on identifying the target behaviour in chapter {{< var chapters.workshops >}}).

Once all ideas were coded, I selected ideas to implement by considering a) whether they could be incorporated into a web-based intervention, b) the priority of the intervention function (determined in objective 2), and c) whether I could feasibly deliver the idea within the time constraints of my DPhil.

#TODO: my results table currently includes _all_ ideas at the moment. But some of these ideas aren't actually intervention components (some are modes of delivery e.g. "provide training" or "networks of champions"). And I've not included all of the ideas in my intervention. Given that I already report all "ideas" in the appendix (and results section of the focus group chapter), I think it might be more useful to just report the intervention components that I've taken forward into the pilot or _could_ include in the website going forward.

#### Results

See table @tbl-int-plan for all {{< var counts.ideas >}} ideas, labelled with the barriers they address, the drivers they target, the intervention functions they use, and whether I could implement them.

### Building the intervention

#### Purpose

The result of my behavioural analysis was a list of components that were abstract. “Reassuring language” or “design that communicates simplicity” could be realised in many different ways. To build a working prototype that could be piloted I had to make these real.

#### Methods and Results

##### Designing the intervention

I began by describing how each intervention component could be realised and how this compared to the existing system (see #tab-int-plan). In doing these comparisons, I looked at how the EQUATOR website is currently, and I made generalisation about how popular reporting guidelines are disseminated, and the content of their Example and Elaboration documents and checklists.

Designing was iterative and collaborative. I included the same members of EQUATOR UK that had participated in the workshops. We met 3 times between November 2022 and January 2023 to discuss intervention design. In our first meeting, we decided which webpages required redesigning, and how webpages should be navigated. On the existing website, authors starting on the home page must visit up to 5 webpages to reach the full reporting guidance. Many authors leave at each step and so few reach the guidance. We redesigned this workflow to reduce this journey to 2 webpages - the EQUATOR home page, and a reporting guideline page containing the full guidance. These different website layouts are visualised in @fig-sankey-b4 and @fig-sankey-after.

Workshop participants then sketched ideas for how the home page and guidance pages could be laid out and where intervention components could be placed. Once participants had agreed on a layout, I created an alpha version of the new website and invited members to comment on it. These were webpages that could be viewed in a browser, but used dummy text and images. After another round of feedback I refined the alpha version, populated it with real text and images, and participants gave feedback again. The new pages can be viewed in @fig-home, @fig-rg-intro, and @fig-discussion, and can be compared with the old pages in @fig-home-b4 and @fig-db-b4.

My intention was to create guideline pages for a sample of the most frequently accessed guidelines so that the website felt real for pilot participants. However, many intervention components involved changing the wording and layout of the guidance itself. Editing multiple guidelines was neither feasible not necessary, as we only needed one edited guideline to pilot the new website.

I selected SRQR as my test guideline to edit because I was familiar with it, having used it when writing up my own research, and because I felt it would make a good guideline to test with (see next chapter for why). I got written permission from Bridget O'Brien, the lead developer or SRQR, and from the publisher. I kept Bridget up to date with my work and invited her feedback.

I began editing SRQR by pasting the text into Microsoft Word and rearranging content into categories: what to write, how/where to write it, what to write if the item wasn't/couldn't be done, why the item is important and to whom, examples. I edited sentences to speak directly to authors. E.g. "Describe X" instead of "Authors should describe X", and to use active voice. This shortened the text and made it clearer that the primary audience is authors.

For composite items I split the sub-items into bulleted lists. E.g.

> For each X, describe:
>
> * X
> * Y
> * Z
>

I rearranged conditional sub-items so that they read "If X, then describe Y", rather than "Describe Y if X". I moved definitions into the glossary and contextual information into notes. I edited the resulting text to join it back together. I edited the tone of voice to add reassuring language. An example of the redesigned guidance can be viewed in #sec-box-item.

After development, I double checked the intervention against the initial list of intervention components to ensure I had covered all of them. I consulted with EQUATOR members to verify that the components were realised as expected and invited another round of feedback.

##### System architecture

When considering architecture options I prioritized technology that could feasibly be maintained by EQUATOR staff or a future PhD student. I looked for tools that would be familiar to early career researchers. I considered DIY website builders (like Wix or Squarespace) but these services can be expensive. Most offer a 'drag and drop' building experience which, although easy to use, is a laborious way of uploading and formatting large amounts of content. Should EQUATOR want to change how an item is presented, they would have to manually edit each item for each reporting guideline. Additionally, our intended intervention changes required custom functionality that wasn't offered by these services (e.g. integration with a DOI minting service, glossary definitions, discussion boards).

Although coding languages like `html` or `javascript` are used by many software developers to create websites, few early career researchers are familiar with them. I decided on `markdown`, an incredibly simple language that can be learnt in a few minutes. It uses asterisks, underscores, and carets to make text **\*\*bold\*\***, _\_italic\__, or ^\^superscript\^^. Headings, URLS, and references are similarly easy, and can be simplified further by using one of many readily available editors that make writing markdown feel like writing a Microsoft Word document.

Many researchers write reproducible manuscripts in markdown using tools like RStudio or Quarto. Quarto can turn markdown into many different file formats including docx, pdf, and html (a website). Quarto documents can be further customised using programming languages commonly used in research, like Ruby or Python. Quarto requires no technical knowledge, is easy to learn, has great documentation, and is open source.

The website is served using Github Pages which is free, beginner friendly, configurable, and integrates (almost) seamlessly with Github's version control system which will already be familiar to many researchers. I wanted EQUATOR to have ultimate control over the website. I also wanted guideline developers to have selective access to edit their own guideline content but not to other guidelines. I have built the website such that each reporting guideline is stored in its own repository on Github, accessible only to its developers. These guideline repositories are then "pulled in" to the main EQUATOR repository, so EQUATOR can double check changes that developers make before allowing them to go live on the site.

The website source code can be viewed at {{< var website-github-repo-url >}} and the website can be viewed at {{< var website-url >}}.

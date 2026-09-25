# Group #5

## Team Members

- Gage Howard
- Nikita Haitsiukevich
- Omar Ibrahim

---

## Algorithm: Aho–Corasick Algorithm

The Aho–Corasick algorithm finds multiple patterns in a larger body of text. It builds a trie from the patterns and uses failure links to keep searching efficiently after a mismatch. Most basic string-searching algorithms look for one pattern at a time, while Aho–Corasick searches for all of them at once. In this project, we will study how the algorithm works, implement it, analyze its time complexity, and compare its performance with other string-matching algorithms.

### Objectives

- Learn how Aho–Corasick searches for many patterns at once.
- See how the trie and failure links work together during a search.
- Analyze the algorithm's time complexity and efficiency.
- Compare it with simpler string-searching algorithms.
- Look at where multi-pattern searching is used in practice.

### Key Tasks

- Research the algorithm and related string-searching methods.
- Implement the trie, failure links, and search.
- Write test cases to check correctness.
- Measure performance across different text sizes and pattern counts.
- Analyze the experimental results alongside the theoretical time complexity.
- Finish the final report and presentation.

### Milestones

- Understand the algorithm fully before starting the main implementation.
- Have a working implementation with initial tests done by the progress update.
- Finish performance testing and analysis before writing the final report.
- Finish and review the report, code, and presentation before each one is due.

---

## Schedule

| Dates | Main Tasks | Additional Tasks / Milestones |
|---|---|---|
| **Week 1:**<br>9/24–9/30 | Read up on Aho–Corasick and get a basic grasp of multi-pattern searching, tries, and failure links. | Look at related string-matching algorithms like Naive Search, KMP, and Rabin–Karp. Split the research among group members. Submit the proposal on 9/25. |
| **Week 2:**<br>10/1–10/7 | Go deeper into how the algorithm works: trie construction, failure links, output states, and time complexity. | Make small example inputs and a first set of test cases. Pick a programming language, code structure, and shared repo. |
| **Week 3:**<br>10/8–10/14 | Start coding. Build the trie and support inserting multiple search patterns. | Start on failure-link construction and test it on small examples where we already know the answer. |
| **Week 4:**<br>10/15–10/21 | Finish the main implementation, including failure links and text searching. | Test overlapping, missing, and repeated patterns, plus patterns that are prefixes of others. Start collecting early performance numbers. |
| **Progress Update:**<br>10/22–10/23 | Check progress against the project plan and write up what we've researched and built so far. | Summarize each member's contributions, the challenges we hit, QA testing, and any roadmap changes. Progress update due 10/23. |
| **Week 5:**<br>10/24–10/30 | Test more thoroughly and compare Aho–Corasick with simpler string-search algorithms. | Run tests on larger and larger texts with different numbers of patterns. Record preprocessing time, search time, and number of matches. |
| **Week 6:**<br>10/31–11/6 | Analyze the performance results and the theoretical time complexity. | Make tables and graphs showing how performance changes as the text grows and the pattern count goes up. Start interpreting the results. |
| **Week 7:**<br>11/7–11/13 | Start the final report. Write the introduction, algorithm explanation, implementation details, and comparison sections. | Add the complexity analysis, benchmark results, real-world applications, and references. Review the code and improve its documentation. |
| **Week 8:**<br>11/14–11/20 | Finalize the report and code. Do a final round of testing and double-check every benchmark result. | Proofread the report, polish the graphs and tables, finish contribution statements and evaluations, and submit. Final submission due 11/20. |
| **Presentation Prep:**<br>11/21–12/4 | Make slides that explain the problem, the algorithm, failure links, complexity, and our results. | Split speaking roles and build a simple visual demo of the trie and failure links in action. |
| **Final Presentation:**<br>12/5–12/10 | Rehearse the full 4–5 minute presentation and make last adjustments. | Make sure everyone understands the algorithm well enough to answer questions. Presentations are on 12/8 and 12/10. |

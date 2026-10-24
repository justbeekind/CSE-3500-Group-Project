# Progress Update

Omar: Personal research, combining researches and findings, drafted rough final report.
Gage: Personal research, combining researches and findings, implemented the trie data structure for future algorithm implementation.
Nikita: Personal research, combining researches and findings, created unit test for algorithm’s development and final testing and performance analysis.

## Milestone Check:

Compared to our expected project timeline, we are not as far ahead as we thought, because the research got held up due to how complex our algorithm seems. We finished up the research and are now working on a rough final report draft and a Python implementation of the algorithm. We also finished up creating the unit tests. We anticipate reaching completion before the deadline to give us time to work on refining and finalizing our final report.

## Roadmap Changes:

Our proposal's milestone was to have a working implementation with initial tests done by the progress update. We have the trie and the unit tests, but the failure links and search are not finished yet.

**Challenges:**
- Failure links and search were not finished because the research took longer than planned and the algorithm turned out to be way more complicated than we thought.
- We haven't started early performance numbers because we're still implementing the code.

**How we plan to tackle them:**
- Finish the code implementation.
- Start performance comparisons with naive search, KMP, and other search algorithms.

**Original proposal changes:**
- We found Boyer-Moore algorithm that could be a good addition to performance comparison.

## Research Progress:

- The Aho-Corasick algorithm is a string search algorithm created by Alfred V. Aho and Margaret J. Corasick at Bell Labs in 1975.
- Aho-Corasick builds a trie of all patterns, adds failure links computed by BFS, and then scans the text once without backtracking. Output links let it report overlapping matches, such as “she,” “he,” and “hers” in “ushers.”
- Compared to other string searching algorithms such as naive search, KMP, Rabin-Karp, and Boyer-Moore, which search for one pattern at a time, Aho-Corasick handles many patterns in one pass at roughly constant cost per character, making it more advantageous at handling multiple string patterns
- The total cost is O(M + n + z). Search time doesn’t depend on the number of patterns k. (M is the total length of all patterns combined, n is the text length, z is the number of matches found, and k is the number of patterns)
- The search is linear because each trie step moves one level down, and each failure step moves a level up. And as it can’t go above the root, there can’t be more failure steps than trie steps. Therefore, at most one trie step per character.
- Limitations: it only does exact matching, the pattern set is fixed so adding or removing patterns usually means a data structure rebuild (which can take a lot of space).
- Applications include fgrep, Snort, ClamAV, content filtering, and bioinformatics.

## Implementation status:

- We are currently working towards a Python implementation of the Aho-Corasick algorithm. So far, we have the unit tests with the trie data structure.

## QA:

We wrote unit tests before starting the implementation, so we can check the correctness as we code.

| Test                              | What it checks                                                                   |
| --------------------------------- | -------------------------------------------------------------------------------- |
| Textbook example (Original Paper) | `he`, `she`, `his`, `hers` in `ushers` finds `she`, `he`, and `hers`             |
| Suffix pattern                    | `she` and `he` in `she` finds both                                               |
| Pattern prefix                    | `a`, `ab`, `abc` in `abc` finds all three                                        |
| Pattern overlap                   | `aa` in `aaaa` finds 3 matches                                                   |
| Failure link                      | `abcd` and `bcx` in `abcx` finds only `bcx`                                      |
| Edge cases                        | Empty text, no matches, one-character text and pattern, pattern longer than text |
| Stress test                       | `aba`, `ba`, `aab` in a 20,000-character `abab...` text                          |

import streamlit as st



from student_auth import load_student_progress, save_student_progress
from chatbot import get_career_guidance


# =========================================================
# DSA INTERVIEW QUESTION BANK
# =========================================================

DSA_QUESTIONS = [
    {
        "id": "two_sum",
        "topic": "Arrays / Hashing",
        "difficulty": "Easy",
        "question": "Find two indices whose values add up to target.",
        "example": "nums = [2, 7, 11, 15], target = 9",
        "answer": "[0, 1]",
        "explanation": "Store previously seen numbers in a dictionary. "
                       "For each number, search for target - number.",
        "solution": {
            "Python": (
                "def two_sum(nums, target):\n"
                "    seen = {}\n"
                "    for i, n in enumerate(nums):\n"
                "        need = target - n\n"
                "        if need in seen:\n"
                "            return [seen[need], i]\n"
                "        seen[n] = i\n"
                "    return []\n\n"
                "print(two_sum([2, 7, 11, 15], 9))"
            ),
            "C++": (
                "#include <iostream>\n#include <vector>\n"
                "#include <unordered_map>\nusing namespace std;\n\n"
                "vector<int> twoSum(vector<int>& a, int target) {\n"
                "    unordered_map<int, int> seen;\n"
                "    for (int i = 0; i < (int)a.size(); i++) {\n"
                "        int need = target - a[i];\n"
                "        if (seen.count(need)) return {seen[need], i};\n"
                "        seen[a[i]] = i;\n"
                "    }\n"
                "    return {};\n"
                "}\n"
            ),
            "Java": (
                "import java.util.*;\n\n"
                "class Solution {\n"
                "    public int[] twoSum(int[] nums, int target) {\n"
                "        Map<Integer, Integer> seen = new HashMap<>();\n"
                "        for (int i = 0; i < nums.length; i++) {\n"
                "            int need = target - nums[i];\n"
                "            if (seen.containsKey(need))\n"
                "                return new int[]{seen.get(need), i};\n"
                "            seen.put(nums[i], i);\n"
                "        }\n"
                "        return new int[]{};\n"
                "    }\n"
                "}\n"
            ),
        },
        "complexity": "Time: O(n), Space: O(n)",
    },
    {
        "id": "reverse_string",
        "topic": "Strings",
        "difficulty": "Easy",
        "question": "Reverse the given string.",
        "example": 'text = "skillora"',
        "answer": '"arolliks"',
        "explanation": "Visit characters from the end to the beginning, "
                       "or use the language's built-in reverse operation.",
        "solution": {
            "Python": 'def reverse_string(text):\n    return text[::-1]\n\nprint(reverse_string("skillora"))',
            "C++": (
                "#include <iostream>\n#include <algorithm>\n"
                "#include <string>\nusing namespace std;\n\n"
                "int main() {\n"
                '    string text = "skillora";\n'
                "    reverse(text.begin(), text.end());\n"
                "    cout << text << endl;\n"
                "}\n"
            ),
            "Java": (
                "class Solution {\n"
                "    public String reverseString(String text) {\n"
                "        return new StringBuilder(text).reverse().toString();\n"
                "    }\n"
                "}\n"
            ),
        },
        "complexity": "Time: O(n), Space: O(n) for a new string",
    },
    {
        "id": "palindrome",
        "topic": "Strings / Two Pointers",
        "difficulty": "Easy",
        "question": "Check whether a string reads the same forward and backward.",
        "example": 'text = "madam"',
        "answer": "True",
        "explanation": "Compare characters from both ends, moving inward.",
        "solution": {
            "Python": (
                "def is_palindrome(text):\n"
                "    return text == text[::-1]\n\n"
                'print(is_palindrome("madam"))'
            ),
            "C++": (
                "#include <iostream>\n#include <algorithm>\n"
                "#include <string>\nusing namespace std;\n"
                "int main() {\n"
                '    string s = "madam";\n'
                "    string r = s;\n"
                "    reverse(r.begin(), r.end());\n"
                "    cout << (s == r) << endl;\n"
                "}\n"
            ),
            "Java": (
                "class Solution {\n"
                "    public boolean isPalindrome(String s) {\n"
                "        return s.equals(new StringBuilder(s).reverse().toString());\n"
                "    }\n"
                "}\n"
            ),
        },
        "complexity": "Time: O(n), Space: O(n) for these solutions",
    },
    {
        "id": "binary_search",
        "topic": "Binary Search",
        "difficulty": "Easy",
        "question": "Find target's index in a sorted array, or return -1.",
        "example": "nums = [1, 3, 5, 7, 9], target = 7",
        "answer": "3",
        "explanation": "Check the middle element and discard half the search range.",
        "solution": {
            "Python": (
                "def binary_search(nums, target):\n"
                "    left, right = 0, len(nums) - 1\n"
                "    while left <= right:\n"
                "        mid = (left + right) // 2\n"
                "        if nums[mid] == target:\n"
                "            return mid\n"
                "        if nums[mid] < target:\n"
                "            left = mid + 1\n"
                "        else:\n"
                "            right = mid - 1\n"
                "    return -1\n\n"
                "print(binary_search([1, 3, 5, 7, 9], 7))"
            ),
            "C++": (
                "int binarySearch(vector<int>& a, int target) {\n"
                "    int l = 0, r = (int)a.size() - 1;\n"
                "    while (l <= r) {\n"
                "        int m = l + (r - l) / 2;\n"
                "        if (a[m] == target) return m;\n"
                "        if (a[m] < target) l = m + 1;\n"
                "        else r = m - 1;\n"
                "    }\n"
                "    return -1;\n"
                "}\n"
            ),
            "Java": (
                "class Solution {\n"
                "    public int search(int[] a, int target) {\n"
                "        int l = 0, r = a.length - 1;\n"
                "        while (l <= r) {\n"
                "            int m = l + (r - l) / 2;\n"
                "            if (a[m] == target) return m;\n"
                "            if (a[m] < target) l = m + 1;\n"
                "            else r = m - 1;\n"
                "        }\n"
                "        return -1;\n"
                "    }\n"
                "}\n"
            ),
        },
        "complexity": "Time: O(log n), Space: O(1)",
    },
    {
        "id": "max_element",
        "topic": "Arrays",
        "difficulty": "Easy",
        "question": "Find the largest element in an array.",
        "example": "nums = [4, 9, 2, 15, 6]",
        "answer": "15",
        "explanation": "Track the largest value seen while scanning the array.",
        "solution": {
            "Python": "def maximum(nums):\n    return max(nums)\n\nprint(maximum([4, 9, 2, 15, 6]))",
            "C++": (
                "#include <algorithm>\n"
                "int maximum(vector<int>& nums) {\n"
                "    return *max_element(nums.begin(), nums.end());\n"
                "}\n"
            ),
            "Java": (
                "int maximum(int[] nums) {\n"
                "    int best = nums[0];\n"
                "    for (int n : nums) best = Math.max(best, n);\n"
                "    return best;\n"
                "}\n"
            ),
        },
        "complexity": "Time: O(n), Space: O(1)",
    },
    {
        "id": "valid_parentheses",
        "topic": "Stack",
        "difficulty": "Medium",
        "question": "Check whether brackets are correctly balanced.",
        "example": 'text = "([])"',
        "answer": "True",
        "explanation": "Push opening brackets onto a stack. Each closing bracket "
                       "must match the most recent opening bracket.",
        "solution": {
            "Python": (
                "def valid_parentheses(text):\n"
                "    stack = []\n"
                "    pairs = {')': '(', ']': '[', '}': '{'}\n"
                "    for ch in text:\n"
                "        if ch in '([{':\n"
                "            stack.append(ch)\n"
                "        elif ch in pairs:\n"
                "            if not stack or stack.pop() != pairs[ch]:\n"
                "                return False\n"
                "    return not stack\n\n"
                'print(valid_parentheses("([])"))'
            ),
            "C++": (
                "#include <stack>\n#include <string>\n"
                "using namespace std;\n"
                "bool valid(string s) {\n"
                "    stack<char> st;\n"
                "    for (char c : s) {\n"
                "        if (c == '(' || c == '[' || c == '{') st.push(c);\n"
                "        else {\n"
                "            if (st.empty()) return false;\n"
                "            char t = st.top(); st.pop();\n"
                "            if ((c == ')' && t != '(') ||\n"
                "                (c == ']' && t != '[') ||\n"
                "                (c == '}' && t != '{')) return false;\n"
                "        }\n"
                "    }\n"
                "    return st.empty();\n"
                "}\n"
            ),
            "Java": (
                "import java.util.*;\n"
                "class Solution {\n"
                "    public boolean isValid(String s) {\n"
                "        Deque<Character> stack = new ArrayDeque<>();\n"
                "        for (char c : s.toCharArray()) {\n"
                "            if (c == '(' || c == '[' || c == '{') stack.push(c);\n"
                "            else {\n"
                "                if (stack.isEmpty()) return false;\n"
                "                char t = stack.pop();\n"
                "                if ((c == ')' && t != '(') ||\n"
                "                    (c == ']' && t != '[') ||\n"
                "                    (c == '}' && t != '{')) return false;\n"
                "            }\n"
                "        }\n"
                "        return stack.isEmpty();\n"
                "    }\n"
                "}\n"
            ),
        },
        "complexity": "Time: O(n), Space: O(n)",
    },
    {
        "id": "factorial",
        "topic": "Recursion / Math",
        "difficulty": "Easy",
        "question": "Calculate the factorial of a non-negative integer n.",
        "example": "n = 5",
        "answer": "120",
        "explanation": "Factorial is the product of all integers from 1 to n; 0! = 1.",
        "solution": {
            "Python": "def factorial(n):\n    result = 1\n    for i in range(2, n + 1):\n        result *= i\n    return result\n\nprint(factorial(5))",
            "C++": (
                "long long factorial(int n) {\n"
                "    long long result = 1;\n"
                "    for (int i = 2; i <= n; i++) result *= i;\n"
                "    return result;\n"
                "}\n"
            ),
            "Java": (
                "long factorial(int n) {\n"
                "    long result = 1;\n"
                "    for (int i = 2; i <= n; i++) result *= i;\n"
                "    return result;\n"
                "}\n"
            ),
        },
        "complexity": "Time: O(n), Space: O(1)",
    },
    {
        "id": "second_largest",
        "topic": "Arrays",
        "difficulty": "Easy",
        "question": "Find the second-largest distinct value.",
        "example": "nums = [10, 5, 8, 10, 3]",
        "answer": "8",
        "explanation": "Track the largest and second-largest distinct values in one pass.",
        "solution": {
            "Python": (
                "def second_largest(nums):\n"
                "    unique = sorted(set(nums))\n"
                "    return unique[-2] if len(unique) >= 2 else None\n\n"
                "print(second_largest([10, 5, 8, 10, 3]))"
            ),
            "C++": (
                "#include <set>\n#include <vector>\n#include <algorithm>\n"
                "int secondLargest(vector<int> a) {\n"
                "    sort(a.begin(), a.end());\n"
                "    a.erase(unique(a.begin(), a.end()), a.end());\n"
                "    return a.size() < 2 ? -1 : a[a.size() - 2];\n"
                "}\n"
            ),
            "Java": (
                "int secondLargest(int[] nums) {\n"
                "    int first = Integer.MIN_VALUE, second = Integer.MIN_VALUE;\n"
                "    for (int n : nums) {\n"
                "        if (n > first) { second = first; first = n; }\n"
                "        else if (n > second && n < first) second = n;\n"
                "    }\n"
                "    return second == Integer.MIN_VALUE ? -1 : second;\n"
                "}\n"
            ),
        },
        "complexity": "Python solution: O(n log n); one-pass approach: O(n)",
    },
    {
        "id": "count_vowels",
        "topic": "Strings",
        "difficulty": "Easy",
        "question": "Count the vowels in a string.",
        "example": 'text = "education"',
        "answer": "5",
        "explanation": "Check each character against a, e, i, o, u.",
        "solution": {
            "Python": (
                "def count_vowels(text):\n"
                "    return sum(ch.lower() in 'aeiou' for ch in text)\n\n"
                'print(count_vowels("education"))'
            ),
            "C++": (
                "#include <string>\n#include <cctype>\n"
                "int countVowels(string s) {\n"
                "    int count = 0;\n"
                "    for (char c : s) {\n"
                "        c = tolower(static_cast<unsigned char>(c));\n"
                "        if (string(\"aeiou\").find(c) != string::npos) count++;\n"
                "    }\n"
                "    return count;\n"
                "}\n"
            ),
            "Java": (
                "int countVowels(String s) {\n"
                "    int count = 0;\n"
                "    for (char c : s.toLowerCase().toCharArray())\n"
                "        if (\"aeiou\".indexOf(c) >= 0) count++;\n"
                "    return count;\n"
                "}\n"
            ),
        },
        "complexity": "Time: O(n), Space: O(1)",
    },
    {
        "id": "fibonacci",
        "topic": "Dynamic Programming",
        "difficulty": "Easy",
        "question": "Return the nth Fibonacci number, with F(0)=0 and F(1)=1.",
        "example": "n = 7",
        "answer": "13",
        "explanation": "Maintain the previous two Fibonacci values instead of "
                       "recomputing earlier terms recursively.",
        "solution": {
            "Python": (
                "def fibonacci(n):\n"
                "    a, b = 0, 1\n"
                "    for _ in range(n):\n"
                "        a, b = b, a + b\n"
                "    return a\n\n"
                "print(fibonacci(7))"
            ),
            "C++": (
                "long long fibonacci(int n) {\n"
                "    long long a = 0, b = 1;\n"
                "    for (int i = 0; i < n; i++) {\n"
                "        long long next = a + b;\n"
                "        a = b; b = next;\n"
                "    }\n"
                "    return a;\n"
                "}\n"
            ),
            "Java": (
                "long fibonacci(int n) {\n"
                "    long a = 0, b = 1;\n"
                "    for (int i = 0; i < n; i++) {\n"
                "        long next = a + b;\n"
                "        a = b; b = next;\n"
                "    }\n"
                "    return a;\n"
                "}\n"
            ),
        },
        "complexity": "Time: O(n), Space: O(1)",
    },
]


# =========================================================
# APTITUDE INTERVIEW QUESTION BANK
# =========================================================

APTITUDE_QUESTIONS = [
    {
        "id": "percentage",
        "topic": "Percentages",
        "question": "What is 20% of 250?",
        "options": ["25", "40", "50", "60"],
        "answer": "50",
        "explanation": "20/100 × 250 = 50.",
    },
    {
        "id": "speed",
        "topic": "Speed and Distance",
        "question": "A car travels 120 km in 2 hours. Average speed?",
        "options": ["40 km/h", "50 km/h", "60 km/h", "80 km/h"],
        "answer": "60 km/h",
        "explanation": "Speed = distance / time = 120 / 2 = 60 km/h.",
    },
    {
        "id": "series",
        "topic": "Number Series",
        "question": "Find the next number: 2, 4, 8, 16, __",
        "options": ["18", "24", "30", "32"],
        "answer": "32",
        "explanation": "Each number is multiplied by 2.",
    },
    {
        "id": "ratio",
        "topic": "Ratio",
        "question": "Ratio is 2:3 and total is 25. Find the smaller part.",
        "options": ["5", "10", "15", "20"],
        "answer": "10",
        "explanation": "Total parts = 5. One part = 25/5 = 5; smaller part = 2×5.",
    },
    {
        "id": "profit",
        "topic": "Profit and Loss",
        "question": "An item costs ₹400 and sells for ₹500. Profit percentage?",
        "options": ["20%", "25%", "30%", "40%"],
        "answer": "25%",
        "explanation": "Profit = 500 - 400 = 100. Profit % = 100/400 × 100 = 25%.",
    },
    {
        "id": "work",
        "topic": "Time and Work",
        "question": "A can finish work in 10 days. What fraction is done in one day?",
        "options": ["1/5", "1/10", "1/20", "10"],
        "answer": "1/10",
        "explanation": "One-day work = 1 / total days = 1/10.",
    },
    {
        "id": "average",
        "topic": "Averages",
        "question": "Find the average of 10, 20, 30.",
        "options": ["15", "20", "25", "30"],
        "answer": "20",
        "explanation": "Average = (10 + 20 + 30) / 3 = 20.",
    },
    {
        "id": "probability",
        "topic": "Probability",
        "question": "What is the probability of getting heads on a fair coin?",
        "options": ["0", "1/4", "1/2", "1"],
        "answer": "1/2",
        "explanation": "One favourable outcome out of two equally likely outcomes.",
    },
    {
        "id": "logic",
        "topic": "Logical Reasoning",
        "question": "All roses are flowers. Which statement must be true?",
        "options": [
            "All flowers are roses",
            "All roses are flowers",
            "No roses are flowers",
            "All flowers are red",
        ],
        "answer": "All roses are flowers",
        "explanation": "It is exactly the statement given in the question.",
    },
    {
        "id": "discount",
        "topic": "Percentages",
        "question": "A ₹1,000 item has a 10% discount. Final price?",
        "options": ["₹100", "₹800", "₹900", "₹990"],
        "answer": "₹900",
        "explanation": "Discount = ₹100. Final price = ₹1,000 - ₹100 = ₹900.",
    },
]


def _get_progress(student_id):
    data = load_student_progress(student_id)

    if not isinstance(data, dict):
        data = {}

    data.setdefault("practice_platform", {})
    p = data["practice_platform"]

    p.setdefault("solved_dsa", [])
    p.setdefault("saved_code", {})
    p.setdefault("aptitude_best_score", 0)
    p.setdefault("aptitude_attempts", 0)

    return data, p


def _save_progress(student_id, data):
    save_student_progress(student_id, data)


def render_dsa_page(student):
    st.title("💻 DSA Interview Preparation")
    st.caption("Practice coding patterns and review interview solutions.")

    student_id = student["id"]
    data, progress = _get_progress(student_id)

    solved = progress["solved_dsa"]
    st.metric("Questions marked solved", f"{len(solved)}/{len(DSA_QUESTIONS)}")

    topic = st.selectbox(
        "Filter by topic",
        ["All"] + sorted({q["topic"] for q in DSA_QUESTIONS}),
    )

    questions = [
        q for q in DSA_QUESTIONS
        if topic == "All" or q["topic"] == topic
    ]

    question = st.selectbox(
        "Select interview question",
        questions,
        format_func=lambda q: f'{q["topic"]} | {q["difficulty"]} | {q["question"]}',
        key="dsa_question_select",
    )

    st.subheader(question["question"])
    st.caption(f'Topic: {question["topic"]} · Difficulty: {question["difficulty"]}')
    st.code(question["example"], language="text")

    language = st.selectbox(
        "Choose language",
        ["Python", "C++", "Java"],
        key="dsa_language_select",
    )

    solution_key = f'{question["id"]}_{language}'
    starter = question["solution"][language]
    previous_code = progress["saved_code"].get(solution_key, starter)

    with st.expander("💡 Interview hint"):
        st.write(question["explanation"])

    with st.expander("✅ View complete solution"):
        st.code(question["solution"][language], language=language.lower())
        st.write("**Complexity:**", question["complexity"])
    
    st.markdown(
        """
        <style>
        div[data-testid="stTextArea"] textarea {
            background-color: #111827 !important;
            color: #f9fafb !important;
            -webkit-text-fill-color: #f9fafb !important;
            caret-color: #60a5fa !important;
            border: 1px solid #475569 !important;
            border-radius: 10px !important;
            font-family: Consolas, monospace !important;
        }

        div[data-testid="stTextArea"] textarea:focus {
            border-color: #60a5fa !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    st.markdown(
        """
        <style>
        /* Code editor: dark background */
        div[data-testid="stTextArea"] textarea {
            background-color: #111827 !important;
            color: #ffffff !important;
            -webkit-text-fill-color: #ffffff !important;
            caret-color: #60a5fa !important;
            border: 1px solid #475569 !important;
            border-radius: 10px !important;
            font-family: Consolas, monospace !important;
    }

    /* Editor focus border */
    div[data-testid="stTextArea"] textarea:focus {
        border: 1px solid #60a5fa !important;
        box-shadow: 0 0 0 1px #60a5fa !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)



    code = st.text_area(
        "Your code editor",
        value=previous_code,
        height=300,
        key=f"editor_{solution_key}",
    )

    st.info(
        "This version displays solutions and saves your code. "
        "It does not compile or execute submitted code."
    )

    if st.button("💾 Save my code", key=f"save_{solution_key}"):
        data, progress = _get_progress(student_id)
        progress["saved_code"][solution_key] = code
        _save_progress(student_id, data)
        st.success("Code saved to your student progress.")

    if st.button("Mark question as solved", key=f"mark_{question['id']}"):
        data, progress = _get_progress(student_id)
        if question["id"] not in progress["solved_dsa"]:
            progress["solved_dsa"].append(question["id"])
            _save_progress(student_id, data)
        st.success("Question marked as solved.")

    if question["id"] in solved:
        st.success("You marked this question as solved.")


def render_aptitude_page(student):
    st.title("🧠 Aptitude Interview Preparation")
    st.caption("Attempt MCQs, check answers and learn from explanations.")

    student_id = student["id"]
    _, progress = _get_progress(student_id)

    st.metric("Best score", f'{progress["aptitude_best_score"]}/{len(APTITUDE_QUESTIONS)}')
    st.write(f'**Quiz attempts:** {progress["aptitude_attempts"]}')

    with st.form("aptitude_interview_quiz"):
        answers = {}

        for index, q in enumerate(APTITUDE_QUESTIONS, start=1):
            st.markdown(f"**Q{index}. [{q['topic']}] {q['question']}**")
            answers[q["id"]] = st.radio(
                "Choose your answer",
                q["options"],
                index=None,
                key=f"aptitude_{q['id']}",
                label_visibility="collapsed",
            )

        submitted = st.form_submit_button("Submit and view results")

    if submitted:
        score = 0
        st.subheader("📊 Your quiz results")

        for index, q in enumerate(APTITUDE_QUESTIONS, start=1):
            selected = answers[q["id"]]

            if selected == q["answer"]:
                score += 1
                st.success(f"Q{index}: Correct!")
            else:
                st.error(f"Q{index}: Incorrect. Correct answer: {q['answer']}")

            st.caption(f"Explanation: {q['explanation']}")

        data, progress = _get_progress(student_id)
        progress["aptitude_attempts"] += 1
        progress["aptitude_best_score"] = max(
            progress["aptitude_best_score"], score
        )
        _save_progress(student_id, data)

        percentage = round(score / len(APTITUDE_QUESTIONS) * 100)
        st.metric("Final score", f"{score}/{len(APTITUDE_QUESTIONS)}")
        st.progress(percentage / 100)
        st.write(f"**Percentage:** {percentage}%")

        if percentage >= 80:
            st.success("Excellent work! Keep practising.")
        elif percentage >= 50:
            st.info("Good attempt. Review the explanations and try again.")
        else:
            st.warning("Keep learning the basics and attempt the quiz again.")

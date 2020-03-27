{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "election_data = os.path.join(\"election_data.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "candidates = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "num_votes = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "percent_votes = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "total_votes = 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(election_data, newline = \"\") as csvfile:\n",
    "    csvreader = csv.reader(csvfile, delimiter = \",\")\n",
    "    csv_header = next(csvreader)\n",
    "\n",
    "    for row in csvreader: \n",
    "        total_votes += 1 \n",
    "\n",
    "        if row[2] not in candidates:\n",
    "            candidates.append(row[2])\n",
    "            index = candidates.index(row[2])\n",
    "            num_votes.append(1)\n",
    "        else:\n",
    "            index = candidates.index(row[2])\n",
    "            num_votes[index] += 1\n",
    "    \n",
    "    for votes in num_votes:\n",
    "        percentage = (votes/total_votes) * 100\n",
    "        percentage = round(percentage)\n",
    "        percentage = \"%.3f%%\" % percentage\n",
    "        percent_votes.append(percentage)\n",
    "    \n",
    "    winner = max(num_votes)\n",
    "    index = num_votes.index(winner)\n",
    "    winning_candidate = candidates[index]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Election Results\n",
      "--------------------------\n",
      "Total Votes: 3521001\n",
      "--------------------------\n",
      "Khan: 63.000% (2218231)\n",
      "Correy: 20.000% (704200)\n",
      "Li: 14.000% (492940)\n",
      "O'Tooley: 3.000% (105630)\n",
      "--------------------------\n",
      "Winner: Khan\n",
      "--------------------------\n"
     ]
    }
   ],
   "source": [
    "print(\"Election Results\")\n",
    "print(\"--------------------------\")\n",
    "print(f\"Total Votes: {str(total_votes)}\")\n",
    "print(\"--------------------------\")\n",
    "for i in range(len(candidates)):\n",
    "    print(f\"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})\")\n",
    "print(\"--------------------------\")\n",
    "print(f\"Winner: {winning_candidate}\")\n",
    "print(\"--------------------------\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "67"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "output = open(\"output.txt\", \"w\")\n",
    "line1 = \"Election Results\"\n",
    "line2 = \"--------------------------\"\n",
    "line3 = str(f\"Total Votes: {str(total_votes)}\")\n",
    "line4 = str(\"--------------------------\")\n",
    "output.write('{}\\n{}\\n{}\\n{}\\n'.format(line1, line2, line3, line4))\n",
    "for i in range(len(candidates)):\n",
    "    line = str(f\"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})\")\n",
    "    output.write('{}\\n'.format(line))\n",
    "line5 = \"--------------------------\"\n",
    "line6 = str(f\"Winner: {winning_candidate}\")\n",
    "line7 = \"--------------------------\"\n",
    "output.write('{}\\n{}\\n{}\\n'.format(line5, line6, line7))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

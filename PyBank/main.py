{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "budget_data = os.path.join(\"budget_data.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "total_months = 0\n",
    "total_pl = 0\n",
    "value = 0\n",
    "change = 0\n",
    "dates = []\n",
    "profits = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(budget_data, newline = \"\") as csvfile:\n",
    "    csvreader = csv.reader(csvfile, delimiter = \",\")\n",
    "\n",
    "    csv_header = next(csvreader)\n",
    "\n",
    "    first_row = next(csvreader)\n",
    "    total_months += 1\n",
    "    total_pl += int(first_row[1])\n",
    "    value = int(first_row[1])\n",
    "    \n",
    "    for row in csvreader:\n",
    "        dates.append(row[0])\n",
    "        \n",
    "        change = int(row[1])-value\n",
    "        profits.append(change)\n",
    "        value = int(row[1])\n",
    "        \n",
    "        total_months += 1\n",
    "\n",
    "        total_pl = total_pl + int(row[1])\n",
    "\n",
    "    greatest_increase = max(profits)\n",
    "    greatest_index = profits.index(greatest_increase)\n",
    "    greatest_date = dates[greatest_index]\n",
    "\n",
    "    greatest_decrease = min(profits)\n",
    "    worst_index = profits.index(greatest_decrease)\n",
    "    worst_date = dates[worst_index]\n",
    "\n",
    "    avg_change = sum(profits)/len(profits)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Financial Analysis\n",
      "---------------------\n",
      "Total Months: 86\n",
      "Total: $38382578\n",
      "Average Change: $-2315.12\n",
      "Greatest Increase in Profits: Feb-2012 ($1926159)\n",
      "Greatest Decrease in Profits: Sep-2013 ($-2196167)\n"
     ]
    }
   ],
   "source": [
    "print(\"Financial Analysis\")\n",
    "print(\"---------------------\")\n",
    "print(f\"Total Months: {str(total_months)}\")\n",
    "print(f\"Total: ${str(total_pl)}\")\n",
    "print(f\"Average Change: ${str(round(avg_change,2))}\")\n",
    "print(f\"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})\")\n",
    "print(f\"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "output = open(\"output.txt\", \"w\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "202"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "line1 = \"Financial Analysis\"\n",
    "line2 = \"---------------------\"\n",
    "line3 = str(f\"Total Months: {str(total_months)}\")\n",
    "line4 = str(f\"Total: ${str(total_pl)}\")\n",
    "line5 = str(f\"Average Change: ${str(round(avg_change,2))}\")\n",
    "line6 = str(f\"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})\")\n",
    "line7 = str(f\"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})\")\n",
    "output.write('{}\\n{}\\n{}\\n{}\\n{}\\n{}\\n{}\\n'.format(line1,line2,line3,line4,line5,line6,line7))"
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

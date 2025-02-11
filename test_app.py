from platform import node


{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "d1ac3a9d-22e4-4558-9558-5cffc689ce45",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pytest\n",
    "from app import app\n",
    "\n",
    "def test_index():\n",
    "    tester=app.test_client()\n",
    "    reponse=tester.get('/')\n",
    "    assert response.status_code==200\n",
    "    assert b\"Hello,World!\" in response.data"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

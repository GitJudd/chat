{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "bot.py",
      "provenance": [],
      "authorship_tag": "ABX9TyMbL4JxchTtAQQaQv2hcuOH",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/GitJudd/chat/blob/main/bo.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4RDezmsEc37I",
        "outputId": "8495a507-1b21-4816-cd89-2ec1ee16717c"
      },
      "source": [
        "!pip install twilio flask requests"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Collecting twilio\n",
            "\u001b[?25l  Downloading https://files.pythonhosted.org/packages/96/42/1a2855d9a1719e5a5f1b2fe62c56674f218c95c030e13d972fa2efa4b588/twilio-6.47.0.tar.gz (460kB)\n",
            "\r\u001b[K     |▊                               | 10kB 4.8MB/s eta 0:00:01\r\u001b[K     |█▍                              | 20kB 8.2MB/s eta 0:00:01\r\u001b[K     |██▏                             | 30kB 5.5MB/s eta 0:00:01\r\u001b[K     |██▉                             | 40kB 2.8MB/s eta 0:00:01\r\u001b[K     |███▋                            | 51kB 3.4MB/s eta 0:00:01\r\u001b[K     |████▎                           | 61kB 4.0MB/s eta 0:00:01\r\u001b[K     |█████                           | 71kB 4.2MB/s eta 0:00:01\r\u001b[K     |█████▊                          | 81kB 4.5MB/s eta 0:00:01\r\u001b[K     |██████▍                         | 92kB 4.8MB/s eta 0:00:01\r\u001b[K     |███████▏                        | 102kB 5.0MB/s eta 0:00:01\r\u001b[K     |███████▉                        | 112kB 5.0MB/s eta 0:00:01\r\u001b[K     |████████▌                       | 122kB 5.0MB/s eta 0:00:01\r\u001b[K     |█████████▎                      | 133kB 5.0MB/s eta 0:00:01\r\u001b[K     |██████████                      | 143kB 5.0MB/s eta 0:00:01\r\u001b[K     |██████████▊                     | 153kB 5.0MB/s eta 0:00:01\r\u001b[K     |███████████▍                    | 163kB 5.0MB/s eta 0:00:01\r\u001b[K     |████████████                    | 174kB 5.0MB/s eta 0:00:01\r\u001b[K     |████████████▉                   | 184kB 5.0MB/s eta 0:00:01\r\u001b[K     |█████████████▌                  | 194kB 5.0MB/s eta 0:00:01\r\u001b[K     |██████████████▎                 | 204kB 5.0MB/s eta 0:00:01\r\u001b[K     |███████████████                 | 215kB 5.0MB/s eta 0:00:01\r\u001b[K     |███████████████▋                | 225kB 5.0MB/s eta 0:00:01\r\u001b[K     |████████████████▍               | 235kB 5.0MB/s eta 0:00:01\r\u001b[K     |█████████████████               | 245kB 5.0MB/s eta 0:00:01\r\u001b[K     |█████████████████▉              | 256kB 5.0MB/s eta 0:00:01\r\u001b[K     |██████████████████▌             | 266kB 5.0MB/s eta 0:00:01\r\u001b[K     |███████████████████▎            | 276kB 5.0MB/s eta 0:00:01\r\u001b[K     |████████████████████            | 286kB 5.0MB/s eta 0:00:01\r\u001b[K     |████████████████████▋           | 296kB 5.0MB/s eta 0:00:01\r\u001b[K     |█████████████████████▍          | 307kB 5.0MB/s eta 0:00:01\r\u001b[K     |██████████████████████          | 317kB 5.0MB/s eta 0:00:01\r\u001b[K     |██████████████████████▉         | 327kB 5.0MB/s eta 0:00:01\r\u001b[K     |███████████████████████▌        | 337kB 5.0MB/s eta 0:00:01\r\u001b[K     |████████████████████████▏       | 348kB 5.0MB/s eta 0:00:01\r\u001b[K     |█████████████████████████       | 358kB 5.0MB/s eta 0:00:01\r\u001b[K     |█████████████████████████▋      | 368kB 5.0MB/s eta 0:00:01\r\u001b[K     |██████████████████████████▍     | 378kB 5.0MB/s eta 0:00:01\r\u001b[K     |███████████████████████████     | 389kB 5.0MB/s eta 0:00:01\r\u001b[K     |███████████████████████████▊    | 399kB 5.0MB/s eta 0:00:01\r\u001b[K     |████████████████████████████▌   | 409kB 5.0MB/s eta 0:00:01\r\u001b[K     |█████████████████████████████▏  | 419kB 5.0MB/s eta 0:00:01\r\u001b[K     |██████████████████████████████  | 430kB 5.0MB/s eta 0:00:01\r\u001b[K     |██████████████████████████████▋ | 440kB 5.0MB/s eta 0:00:01\r\u001b[K     |███████████████████████████████▎| 450kB 5.0MB/s eta 0:00:01\r\u001b[K     |████████████████████████████████| 460kB 5.0MB/s \n",
            "\u001b[?25hRequirement already satisfied: flask in /usr/local/lib/python3.6/dist-packages (1.1.2)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.6/dist-packages (2.23.0)\n",
            "Requirement already satisfied: six in /usr/local/lib/python3.6/dist-packages (from twilio) (1.15.0)\n",
            "Requirement already satisfied: pytz in /usr/local/lib/python3.6/dist-packages (from twilio) (2018.9)\n",
            "Collecting PyJWT>=1.4.2\n",
            "  Downloading https://files.pythonhosted.org/packages/87/8b/6a9f14b5f781697e51259d81657e6048fd31a113229cf346880bb7545565/PyJWT-1.7.1-py2.py3-none-any.whl\n",
            "Requirement already satisfied: click>=5.1 in /usr/local/lib/python3.6/dist-packages (from flask) (7.1.2)\n",
            "Requirement already satisfied: itsdangerous>=0.24 in /usr/local/lib/python3.6/dist-packages (from flask) (1.1.0)\n",
            "Requirement already satisfied: Werkzeug>=0.15 in /usr/local/lib/python3.6/dist-packages (from flask) (1.0.1)\n",
            "Requirement already satisfied: Jinja2>=2.10.1 in /usr/local/lib/python3.6/dist-packages (from flask) (2.11.2)\n",
            "Requirement already satisfied: chardet<4,>=3.0.2 in /usr/local/lib/python3.6/dist-packages (from requests) (3.0.4)\n",
            "Requirement already satisfied: idna<3,>=2.5 in /usr/local/lib/python3.6/dist-packages (from requests) (2.10)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.6/dist-packages (from requests) (2020.6.20)\n",
            "Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /usr/local/lib/python3.6/dist-packages (from requests) (1.24.3)\n",
            "Requirement already satisfied: MarkupSafe>=0.23 in /usr/local/lib/python3.6/dist-packages (from Jinja2>=2.10.1->flask) (1.1.1)\n",
            "Building wheels for collected packages: twilio\n",
            "  Building wheel for twilio (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for twilio: filename=twilio-6.47.0-py2.py3-none-any.whl size=1217344 sha256=51251a80a692e2608d442350531089bdce57f9a1ae3ac7a13e8ac91363b4855d\n",
            "  Stored in directory: /root/.cache/pip/wheels/8f/03/da/f5b1289ebc34ff99b3f90f2c7d3a3bcf6c838cf7ff51b9017f\n",
            "Successfully built twilio\n",
            "Installing collected packages: PyJWT, twilio\n",
            "Successfully installed PyJWT-1.7.1 twilio-6.47.0\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "V2ajfRNKc5_V"
      },
      "source": [
        "from flask import Flask, request\n",
        "import requests\n",
        "from twilio.twiml.messaging_response import MessagingResponse\n",
        "\n",
        "app = Flask(__name__)\n",
        "\n",
        "\n",
        "@app.route('/bot', methods=['POST'])\n",
        "def bot():\n",
        "    incoming_msg = request.values.get('Body', '').lower()\n",
        "    resp = MessagingResponse()\n",
        "    msg = resp.message()\n",
        "    responded = False\n",
        "    if 'quote' in incoming_msg:\n",
        "        # return a quote\n",
        "        r = requests.get('https://api.quotable.io/random')\n",
        "        if r.status_code == 200:\n",
        "            data = r.json()\n",
        "            quote = f'{data[\"content\"]} ({data[\"author\"]})'\n",
        "        else:\n",
        "            quote = 'I could not retrieve a quote at this time, sorry.'\n",
        "        msg.body(quote)\n",
        "        responded = True\n",
        "    if 'cat' in incoming_msg:\n",
        "        # return a cat pic\n",
        "        msg.media('https://cataas.com/cat')\n",
        "        responded = True\n",
        "    if not responded:\n",
        "        msg.body('I only know about famous quotes and cats, sorry!')\n",
        "    return str(resp)"
      ],
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4imdwOeLdYBc",
        "outputId": "68b05440-ac81-4132-dc05-07e647d89e8d"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "python3: can't open file 'bot.py': [Errno 2] No such file or directory\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "-sEggoH-dntF"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}
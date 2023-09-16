{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP2Y7PQK2UYfNI/rkUQrV+6",
      "include_colab_link": "true"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
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
        "<a href=\"https://colab.research.google.com/github/lula0610/linebot/blob/main/main.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": "null",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PcgcMka13Y-q",
        "outputId": "11e29903-804c-43cf-9aab-2149e9a88690"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting line-bot-sdk\n",
            "  Downloading line_bot_sdk-3.1.0-py2.py3-none-any.whl (729 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m729.1/729.1 kB\u001b[0m \u001b[31m16.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting requests==2.31.0 (from line-bot-sdk)\n",
            "  Downloading requests-2.31.0-py3-none-any.whl (62 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m62.6/62.6 kB\u001b[0m \u001b[31m7.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: aiohttp==3.8.4 in /usr/local/lib/python3.10/dist-packages (from line-bot-sdk) (3.8.4)\n",
            "Requirement already satisfied: future in /usr/local/lib/python3.10/dist-packages (from line-bot-sdk) (0.18.3)\n",
            "Requirement already satisfied: pydantic<2,>=1.10.5 in /usr/local/lib/python3.10/dist-packages (from line-bot-sdk) (1.10.9)\n",
            "Collecting aenum>=3.1.11 (from line-bot-sdk)\n",
            "  Downloading aenum-3.1.15-py3-none-any.whl (137 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m137.6/137.6 kB\u001b[0m \u001b[31m18.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: python-dateutil>=2.5.3 in /usr/local/lib/python3.10/dist-packages (from line-bot-sdk) (2.8.2)\n",
            "Collecting Deprecated (from line-bot-sdk)\n",
            "  Downloading Deprecated-1.2.14-py2.py3-none-any.whl (9.6 kB)\n",
            "Requirement already satisfied: attrs>=17.3.0 in /usr/local/lib/python3.10/dist-packages (from aiohttp==3.8.4->line-bot-sdk) (23.1.0)\n",
            "Requirement already satisfied: charset-normalizer<4.0,>=2.0 in /usr/local/lib/python3.10/dist-packages (from aiohttp==3.8.4->line-bot-sdk) (2.0.12)\n",
            "Requirement already satisfied: multidict<7.0,>=4.5 in /usr/local/lib/python3.10/dist-packages (from aiohttp==3.8.4->line-bot-sdk) (6.0.4)\n",
            "Requirement already satisfied: async-timeout<5.0,>=4.0.0a3 in /usr/local/lib/python3.10/dist-packages (from aiohttp==3.8.4->line-bot-sdk) (4.0.2)\n",
            "Requirement already satisfied: yarl<2.0,>=1.0 in /usr/local/lib/python3.10/dist-packages (from aiohttp==3.8.4->line-bot-sdk) (1.9.2)\n",
            "Requirement already satisfied: frozenlist>=1.1.1 in /usr/local/lib/python3.10/dist-packages (from aiohttp==3.8.4->line-bot-sdk) (1.3.3)\n",
            "Requirement already satisfied: aiosignal>=1.1.2 in /usr/local/lib/python3.10/dist-packages (from aiohttp==3.8.4->line-bot-sdk) (1.3.1)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests==2.31.0->line-bot-sdk) (3.4)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests==2.31.0->line-bot-sdk) (1.26.16)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests==2.31.0->line-bot-sdk) (2023.5.7)\n",
            "Requirement already satisfied: typing-extensions>=4.2.0 in /usr/local/lib/python3.10/dist-packages (from pydantic<2,>=1.10.5->line-bot-sdk) (4.6.3)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.5.3->line-bot-sdk) (1.16.0)\n",
            "Requirement already satisfied: wrapt<2,>=1.10 in /usr/local/lib/python3.10/dist-packages (from Deprecated->line-bot-sdk) (1.14.1)\n",
            "Installing collected packages: aenum, requests, Deprecated, line-bot-sdk\n",
            "  Attempting uninstall: requests\n",
            "    Found existing installation: requests 2.27.1\n",
            "    Uninstalling requests-2.27.1:\n",
            "      Successfully uninstalled requests-2.27.1\n",
            "\u001b[31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.\n",
            "google-colab 1.0.0 requires requests==2.27.1, but you have requests 2.31.0 which is incompatible.\u001b[0m\u001b[31m\n",
            "\u001b[0mSuccessfully installed Deprecated-1.2.14 aenum-3.1.15 line-bot-sdk-3.1.0 requests-2.31.0\n"
          ]
        }
      ],
      "source": [
        "!pip install line-bot-sdk"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from linebot import LineBotApi\n",
        "from linebot.models import TextSendMessage"
      ],
      "metadata": {
        "id": "bi0QiNM730fJ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "line_bot_api = LineBotApi('N5tqS9SVqIydfsq2f1iGUYCxR+7POzkA4l97izp93CvHr7IFfGmQ9FoBB5pikXoKv3giwVu2QRgGHOb/HKellAecTvyxTtacd5Z3vtzAgptxzvSd6wr/T/iPKCNoy4pxMJ25iXJ9Zqu2FuHD5TwtIQdB04t89/1O/w1cDnyilFU=')\n",
        "USER_ID = \"Ue1dc70357d219f0356e50b8fbbca6967\"\n",
        "messages = TextSendMessage(text=\"https://www.youtube.com/watch?v=DMk1if63aXg&feature=youtu.be\")\n",
        "line_bot_api.push_message(USER_ID,messages= messages)"
      ],
      "metadata": {
        "id": "zcBAGZCL4M2o",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "e2ac29cd-7921-429b-cfed-1f5b7e7b2bca"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-4-21fa1c0193aa>:1: LineBotSdkDeprecatedIn30: Call to deprecated class LineBotApi. (Use v3 class; linebot.v3.<feature>. See https://github.com/line/line-bot-sdk-python/blob/master/README.rst for more details.) -- Deprecated since version 3.0.0.\n",
            "  line_bot_api = LineBotApi('N5tqS9SVqIydfsq2f1iGUYCxR+7POzkA4l97izp93CvHr7IFfGmQ9FoBB5pikXoKv3giwVu2QRgGHOb/HKellAecTvyxTtacd5Z3vtzAgptxzvSd6wr/T/iPKCNoy4pxMJ25iXJ9Zqu2FuHD5TwtIQdB04t89/1O/w1cDnyilFU=')\n",
            "<ipython-input-4-21fa1c0193aa>:4: LineBotSdkDeprecatedIn30: Call to deprecated method push_message. (Use 'from linebot.v3.messaging import MessagingApi' and 'MessagingApi(...).push_message(...)' instead. See https://github.com/line/line-bot-sdk-python/blob/master/README.rst for more details.) -- Deprecated since version 3.0.0.\n",
            "  line_bot_api.push_message(USER_ID,messages= messages)\n"
          ]
        }
      ]
    }
  ]
}

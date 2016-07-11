# distributed wellbeing

![](images/Einstein.png)

*It can't be bargained with; it can't be reasoned with; it doesn't feel pity, or remorse, or fear, and it absolutely will not stop, ever, until wellbeing is distributed.*

# introduction

## distributed wellbeing

Imagine a mechanism of voting that does not involve placing a pictogram on paper into a secure box for scrutiny by a single government. Imagine one that involves running the government software of your choice. Imagine concurrent governments and distributed nations.

## analysis of individuals

There exist useful metrics for analysis of individuals. These metrics can include measures of psychological and financial wellbeing. For the former, a simple measure could be sentiment analysis of social media expressions; for the latter, a simple measure could be somewhat similar to measurements of benefits needs. Proxy-trust networks can reduce uncertainties.

## distributed wellbeing

The metrics for description of individuals can be used to distribute wellbeing in various forms. One form could be alerts for and prioritisation of psychological treatment, be that for everything from treatment of depression to treatment of religious fundamentalism. Another form could be distribution of wealth via Bitcoin using a donated fund owned by the distributed wellbeing system.

## precidents

There exist multiple decentralized, distributed systems running on the internet. There is distributed currency in the form of Bitcoin, there is distributed communications in the form of Tox, there is distributed data in the form of BitTorrent and there is distributed information and interaction in the form of Tor and onion routing. Analysis of individuals and wellbeing can be distributed in a decentralized way.

## evolution of government

Revolution is hard and often unsuccessful. Evolution is easier and is more amenable to change and optimisation. Consider distributed wellbeing as the possible beginnings of an automated system of government that can run (to varying extents) concurrently with existing government and other distributed wellbeing systems.

## project goals

A goal of this project is to collate thoughts and methods of describing individuals in terms of wellbeing needs, with two possible metrics being psychological wellbeing and financial wellbeing. Another goal of this project is to create free, open software that is decentralized and capable of analysis of individuals and automated flagging and prioritisation of psychological wellbeing needs and automated receipt of and distribution of wealth.

# setup

- <https://github.com/wdbm/abstraction>

```Bash
sudo pip install distributed_wellbeing
git clone https://github.com/wdbm/distributed_wellbeing.git
cd distributed_wellbeing
```

# usage

## sentiment analysis of tweets

```Bash
./sentiment_tweets.py --help
./sentiment_tweets.py
```

## distributed wellbeing prototype

```Bash
./distributed_wellbeing.py --verbose
```

# decentralization

In peer-to-peer decentralization, push technologies like UDP broadcasts can be used, whereby each client sends a heartbeat packet every so often on the network for others to receive. The module socket is useful for this.

Bitcoin clients use several methods to locate other clients. A primary method is to use a list of nodes from a previous connection to the network. This works well generally for all connections except for the first connection and a connection that follows a long time of disconnection. With no local list of nodes, DNS seeds, maintained hosts, can be queried. A hardcoded list of nodes can be considered also. An old method was to use an IRC server that worked in a way similar to that of BitTorrent trackers.

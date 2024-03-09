from django.shortcuts import render

shoping_katagori = ["Ethical Hacking Black Book", "Everest-Ewn", "Flipper Zero", "HackRF"]

shoping_list = [
    {
        "name": "Ethical Hacking Black Book",
        "abaut": "Written in an easy to understand style, this book provides a complete guide to Ethical Hacking with practicals.This ethical hacking book covers complete Kali Linux, Ethical Hacking, Cyber Security",
        "img": "ethical-hacking.jpeg"
    },
    {
        "name": "Everest-Ewn",
        "abaut": "Everest EWN-689N 300Mbps Wireless Adapter (1Km Range)",
        "img": "everest-ewn.jpeg",
    },
    {
        "name": "Flipper Zero",
        "abaut": "Flipper Zero Multi-tool Device for Geeks Flipper Zero is a portable multi-tool for pentesters and geeks in a toy-like body. It loves hacking digital stuff, such as radio protocols, access control systems, hardware, and more.",
        "img": "flipper-zero.jpeg",
    },
    {
        "name": "HackRF",
        "abaut": "HackRF One from Great Scott Gadgets is a Software Defined Radio peripheral capable of transmission or reception of radio signals from 1 MHz to 6 GHz. Designed to enable test and development of modern and next generation radio technologies, HackRF One is an open source hardware platform that can be used as a USB peripheral or programmed for stand-alone operation.",
        "img": "hackrf.jpeg",
    }
]



def basket_list(request):
    data = {
        "shoping_katagori": shoping_katagori,
        "shoping_list": shoping_list
    }
    return render(request, "basket.html", data)


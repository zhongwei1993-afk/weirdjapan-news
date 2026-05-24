---
title: "Every Phone in Japan Screams 15 Seconds Before an Earthquake"
description: "Japan's J-Alert system detects P-waves and pushes a warning to every device within range. 15 seconds is enough to drop, cover, and hold."
pubDate: 2026-05-01
category: "Tech"
heroImageUrl: "https://commons.wikimedia.org/wiki/Special:FilePath/Earthquake%20Aftermath%20in%20Misawa%20and%20Hachinohe%2C%20Japan%20Image%201%20of%207.jpg?width=1600"
heroImageAlt: "Earthquake Aftermath in Misawa and Hachinohe, Japan Image 1 of 7"
heroImageCredit: "Image via Wikimedia Commons"
heroImageCreditUrl: "https://commons.wikimedia.org/wiki/File%3AEarthquake_Aftermath_in_Misawa_and_Hachinohe%2C_Japan_Image_1_of_7.jpg"
---

# Every Phone in Japan Screams 15 Seconds Before an Earthquake

You are sitting in a Tokyo café. Your iPhone, your neighbor's Android, the speakers in the convenience store next door, the television in the corner, and every device with a Japanese SIM card within a hundred kilometers all make the same noise at the same instant: a flat, mechanical two-tone alarm — *pien, pien, pien-pien-pien*. Three seconds later the floor moves. Nobody screams. The barista finishes pouring the espresso, hands it across the counter, and waits for the shaking to stop.

This is the Japan Meteorological Agency's Earthquake Early Warning system, and it has been running, more or less invisibly, since October 2007.

## The Physics That Make It Possible

Earthquakes travel as two main wave types. The P-wave — primary, compressional — moves through bedrock at roughly six kilometers per second. The S-wave — secondary, shear — follows at about three. The P-wave does little damage. The S-wave is the one that knocks plates off shelves and bridges off piers.

That two-to-one speed difference is the entire opportunity. If you can detect a P-wave at the epicenter and broadcast a warning faster than the S-wave can travel to the receiver, you have bought somebody a few seconds. For an earthquake a hundred kilometers away, that gap is around twenty seconds. For a thousand kilometers away, well over a minute.

The Japan Meteorological Agency, known as JMA, built a national system to exploit exactly that gap. It is called **Kinkyu Jishin Sokuho** — 緊急地震速報 — the Earthquake Early Warning, or EEW for short. It has been operationally broadcasting to the public since October 1, 2007, which makes it older than the iPhone in your hand.

## The Network That Feeds the Warning

Japan sits on more than 1,400 seismometer stations. The JMA operates several hundred of its own; the rest belong to the National Research Institute for Earth Science and Disaster Resilience (NIED), which runs the Hi-net and K-NET observation grids. Together they blanket the country at roughly one sensor per twenty-five-kilometer square. There is almost nowhere on the archipelago more than a short drive from a buried accelerometer.

When P-waves arrive at the nearest stations, the system does three things in roughly one second: it locates the epicenter, estimates the magnitude, and calculates the expected JMA Shindo intensity at every populated grid cell in the country. Shindo is Japan's seven-level shaking scale — distinct from magnitude — and it is what people actually care about. A magnitude 7 quake under the seabed is interesting. A Shindo 6 quake under your office is not.

If the projected intensity for any inhabited region hits **Shindo 5-lower or higher**, the public warning triggers. Below that threshold, only an advanced warning goes out to subscribed industries — railways, utilities, factories, hospitals. Above it, every device in the projected shake zone gets pinged.

The typical lead time is five to sixty seconds, depending entirely on how far the receiver sits from the epicenter. Sometimes it is two seconds. Sometimes it is ninety. For an earthquake directly below your building, the warning arrives at the same instant as the shaking, which is a known and accepted limitation. You cannot outrun physics.

## How the Warning Reaches You

The delivery side is where the system stops being a research project and becomes infrastructure. Within one to two seconds of the JMA trigger, the warning is simultaneously pushed through four parallel channels.

**NHK**, the public broadcaster, cuts into live TV and radio with an automated overlay. The tone — flat, slightly distressed, instantly recognizable — was composed specifically not to sound like any normal alert. Japanese residents call it *pien-pien*. Most can identify it from a single beat across a crowded room.

**Cell Broadcast Service (CBS)** pushes a short two-line message to every active phone in the affected geographic cell. It bypasses the normal data network, so it works even when towers are saturated. The text is sparse: 緊急地震速報, followed by epicenter and estimated magnitude. Every phone with a Japanese SIM from the major carriers — Docomo, KDDI/au, SoftBank, Rakuten — receives it by default, with the alert sound forced to maximum volume regardless of silent-mode settings.

**J-Alert**, the national civil-defense system, fires outdoor loudspeakers and triggers automated cut-ins on community FM stations and disaster-radio receivers in homes.

**Private industry feeds** go to railway operators, elevator companies, surgical theaters, semiconductor fabs, and anyone else who has paid for a millisecond-accurate dedicated line.

Foreign tourists are the gap in the system. A phone roaming on a foreign SIM may not receive CBS reliably, and the Japanese-language alert is useless if you cannot read it. JMA's recommended workaround is the free **Safety Tips** app, published by the Japan Tourism Agency, which mirrors EEW alerts in English, Chinese, Korean, and a dozen other languages. It is, quietly, one of the most important downloads a visitor can make.

## What Happens in Those Seconds

This is the part that gets undersold abroad. The warning is not the point. The warning is the trigger for a cascade of automated and rehearsed human actions, all designed to fit inside a fifteen-second window.

**Shinkansen bullet trains** have run on automatic seismic braking since long before EEW existed, but the modern system integrates the JMA feed directly into the train control network. A train cruising at 320 km/h receives the trigger, cuts traction power, and engages emergency braking. From full speed to a complete stop takes three to four minutes — but the deceleration starts before the rails themselves begin to whip. The widely cited statistic: zero passenger deaths from earthquake-induced derailment since the Shinkansen began operating in 1964. The 2011 Tohoku quake derailed exactly one out-of-service train. Every revenue train was either already stopped or stopping.

**Elevators** receive the warning and dock at the nearest floor before shaking arrives, opening their doors. **Surgeons** pause and stabilize instruments. **Factory presses, robotic welders, and crane operations** halt automatically. **Gas valves** in millions of homes shut via the household intensity-sensitive meter. **Schools** drill *drop-cover-hold* the way American schools once drilled fire — every child in Japan has done it dozens of times by the time they reach middle school.

In Tokyo on March 11, 2011, the EEW system gave the city between **sixty and eighty seconds** of warning before the destructive S-waves arrived from the Tohoku epicenter four hundred kilometers north. Eighty seconds is enough to land an elevator, halt a press, stop a train, sit down, and remember which doorway is structural.

## The Limits, the Failures, and What Comes Next

The system is not perfect, and the JMA does not pretend otherwise.

The most-cited failure happened in August 2013, when an EEW for an Awaji Island quake estimated magnitude 7.8 and triggered nationwide alerts. The actual quake came in at magnitude 5.4. A faulty sensor reading had been compounded by the algorithm. JMA issued a public apology, revised the calibration, and the false-alarm rate has stayed low since. The agency publishes a quarterly report on every missed and over-warned event, which is in itself a quietly Japanese institutional behavior.

Citizen apps have filled the remaining gaps. **Yurekuru Call** is the older standard — clean interface, customizable Shindo threshold, used by tens of millions. **NERV Disaster Prevention**, run by a small private company named after the *Evangelion* anime organization, has become the cult favorite for its faster push pipeline and elegant maps. Both pull directly from JMA's data feed.

Looming over all of this is the **Nankai Trough Megaquake** forecast. Japan's Headquarters for Earthquake Research Promotion currently puts the probability of a magnitude 8-to-9 event along the Nankai fault at **70 to 80 percent within the next thirty years**. EEW will give coastal cities tens of seconds. The tsunami warning, which runs on the same infrastructure, will give them tens of minutes. Both numbers are taken extremely seriously by every prefecture from Shizuoka to Kyushu.

For comparison: the United States launched its own equivalent, **ShakeAlert**, on the West Coast in 2018. It uses similar P-wave detection but covers only California, Oregon, and Washington, with roughly a tenth of Japan's sensor density. It is a good system. It is not yet a national reflex.

## TL;DR

Japan's Earthquake Early Warning system detects the fast, harmless P-wave at one of 1,400+ seismometers, calculates intensity in under a second, and pushes a warning to every phone, TV, radio, train, elevator, and factory in the projected shake zone — typically five to sixty seconds before the destructive S-wave arrives. It is twenty years old, costs the public nothing, and is the reason no Shinkansen passenger has ever died in an earthquake. Foreign visitors should install the Safety Tips app on arrival.

---

## Related on WeirdJapan

- [Why the Shinkansen Cleans Itself in 7 Minutes](/blog/shinkansen-7-min-cleaning)
- [Tokyo's Underground Rivers Nobody Talks About](/blog/tokyo-underground-rivers)
- [The Train That Apologized for Leaving 20 Seconds Early](/blog/apology-train-20-seconds)
- [Why Tokyo Trains Are Almost Completely Silent](/blog/silent-trains-tokyo)
- [Japan's National Lost-Umbrella System](/blog/lost-umbrella-system)
- [The Taxi Doors That Open By Themselves](/blog/taxi-doors-automatic)

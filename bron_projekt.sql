-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1
-- Время создания: Май 28 2025 г., 17:21
-- Версия сервера: 10.4.32-MariaDB
-- Версия PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `bron_projekt`
--

-- --------------------------------------------------------

--
-- Структура таблицы `cabinets`
--

CREATE TABLE `cabinets` (
  `id` int(11) NOT NULL,
  `Cabinet` varchar(255) DEFAULT NULL,
  `Reservation (name)` varchar(255) DEFAULT NULL COMMENT 'Real name',
  `Subject` varchar(255) DEFAULT NULL,
  `Time` time DEFAULT NULL COMMENT 'Start time',
  `Time_end` time DEFAULT NULL COMMENT 'End time',
  `Date` date DEFAULT NULL COMMENT 'Date',
  `Grupp` varchar(255) DEFAULT NULL COMMENT 'Grupp',
  `IsDefense` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Дамп данных таблицы `cabinets`
--

INSERT INTO `cabinets` (`id`, `Cabinet`, `Reservation (name)`, `Subject`, `Time`, `Time_end`, `Date`, `Grupp`, `IsDefense`) VALUES
(134, 'C311', 'alevtina.serova', 'Inglise keel', '08:15:00', '09:45:00', '2025-06-02', 'JPIT24', 0),
(135, 'C311', 'alevtina.serova', 'Inglise keel', '12:10:00', '13:40:00', '2025-06-06', 'JPIT24', 0),
(136, 'C311', 'alevtina.serova', 'Inglise keel', '13:50:00', '15:20:00', '2025-06-06', 'JPIT24', 0),
(137, 'C304', 'heidi.edela', 'MAJANDUSE ALUSED', '09:55:00', '11:25:00', '2025-06-02', 'JPIT24', 0),
(138, 'C304', 'ilia.bogatyrev', 'Matemaatika', '08:15:00', '09:45:00', '2025-06-03', 'JPIT24', 0),
(139, 'C304', 'ilia.bogatyrev', 'Matemaatika', '12:10:00', '13:40:00', '2025-06-04', 'JPIT24', 0),
(140, 'C304', 'jaanek.pahka', 'Ühiskonnaõpetus', '09:55:00', '11:25:00', '2025-06-03', 'JPIT24', 0),
(141, 'C304', 'jaanek.pahka', 'Ühiskonnaõpetus', '09:55:00', '11:25:00', '2025-06-04', 'JPIT24', 0),
(142, 'C211', 'viivi.treier', 'Eesti keel teise keelena', '08:15:00', '09:45:00', '2025-06-04', 'JPIT24', 0),
(143, 'C211', 'viivi.treier', 'Eesti keel teise keelena', '12:10:00', '13:40:00', '2025-06-05', 'JPIT24', 0),
(144, 'C211', 'viivi.treier', 'Eesti keel teise keelena', '13:50:00', '15:20:00', '2025-06-05', 'JPIT24', 0),
(145, 'C211', 'viivi.treier', 'Eesti keel teise keelena', '08:15:00', '09:45:00', '2025-06-06', 'JPIT24', 0),
(146, 'C211', 'viivi.treier', 'Eesti keel teise keelena', '09:55:00', '11:25:00', '2025-06-06', 'JPIT24', 0),
(147, 'C214', 'aleksander.pulver', 'Programmerimise alused', '08:15:00', '09:45:00', '2025-06-05', 'JPIT24', 0),
(148, 'C214', 'aleksander.pulver', 'Programmerimise alused', '09:55:00', '11:25:00', '2025-06-05', 'JPIT24', 0),
(149, 'C214', 'aleksander.pulver', 'Programmerimise alused', '09:55:00', '11:25:00', '2025-05-29', 'JPIT24', 1),
(150, 'C214', 'aleksander.pulver', 'Programmerimise alused', '08:15:00', '09:45:00', '2025-05-29', 'JPIT24', 1),
(151, 'C214', 'aleksander.pulver', 'IT-korraldus', '12:10:00', '13:40:00', '2025-05-29', 'JPITE21', 0),
(152, 'C214', 'aleksander.pulver', 'IT-korraldus', '13:50:00', '15:20:00', '2025-05-29', 'JPITE21', 0),
(153, 'C214', 'aleksander.pulver', 'IT-korraldus', '08:15:00', '09:45:00', '2025-06-02', 'JPITE21', 0),
(154, 'C214', 'aleksander.pulver', 'IT-korraldus', '09:55:00', '11:25:00', '2025-06-02', 'JPITE21', 1),
(155, 'C214', 'aleksander.pulver', 'IT-korraldus', '12:10:00', '13:40:00', '2025-06-02', 'JPITE21', 1),
(156, 'C214', 'aleksander.pulver', 'IT-korraldus', '13:50:00', '15:20:00', '2025-06-02', 'JPITE21', 0),
(157, 'F245', 'aleksander.pulver', 'Kutseeksam', '08:00:00', '16:00:00', '2025-06-03', 'JPITE21', 1),
(158, 'C214', 'aleksander.pulver', 'Portfoolio koostamine', '08:15:00', '09:45:00', '2025-06-10', 'JPJUE23', 0),
(159, 'C214', 'aleksander.pulver', 'Portfoolio koostamine', '09:55:00', '11:25:00', '2025-06-10', 'JPJUE23', 0),
(160, 'C214', 'aleksander.pulver', 'Programmerimise alused', '09:55:00', '11:25:00', '2025-06-12', 'JPIT24', 0),
(161, 'C214', 'aleksander.pulver', 'Programmerimise alused', '08:15:00', '09:45:00', '2025-06-12', 'JPIT24', 0),
(162, 'C304', 'ilia.bogatyrev', 'Füüsika', '08:15:00', '09:45:00', '2025-06-10', 'JPEPE24', 0),
(163, 'C304', 'ilia.bogatyrev', 'Füüsika', '09:55:00', '11:25:00', '2025-06-10', 'JPEPE24', 0),
(164, 'C204', 'anna.torn', 'Bioloogia', '12:10:00', '13:40:00', '2025-06-02', 'JPTV24', 0),
(165, 'C204', 'anna.torn', 'Keemia', '08:15:00', '09:45:00', '2025-06-03', 'JPTV24', 0),
(166, 'C204', 'anna.torn', 'Keemia', '09:55:00', '11:25:00', '2025-06-03', 'JPTV24', 0),
(167, 'C204', 'anna.torn', 'Keemia', '09:55:00', '11:25:00', '2025-06-10', 'JPTV24', 0),
(168, 'C204', 'anna.torn', 'Keemia', '08:15:00', '09:45:00', '2025-06-10', 'JPTV24', 0),
(169, 'C204', 'anna.torn', 'Bioloogia', '12:10:00', '13:40:00', '2025-06-10', 'JPEPE24', 0),
(170, 'C204', 'anna.torn', 'Bioloogia', '13:50:00', '15:20:00', '2025-06-10', 'JPEPE24', 0),
(171, 'E201', 'svetlana.avdejeva', 'Laboriseadmed ja töövahendid', '08:15:00', '09:45:00', '2025-05-29', 'JPLB24', 0),
(172, 'E201', 'svetlana.avdejeva', 'Laboriseadmed ja töövahendid', '09:55:00', '11:25:00', '2025-05-29', 'JPLB24', 0),
(173, 'E201', 'svetlana.avdejeva', 'Laboriseadmed ja töövahendid', '12:10:00', '13:40:00', '2025-05-29', 'JPLB24', 0),
(174, 'E201', 'svetlana.avdejeva', 'Laboriseadmed ja töövahendid', '12:10:00', '13:40:00', '2025-05-30', 'JPLB24', 0),
(175, 'E201', 'svetlana.avdejeva', 'Laboriseadmed ja töövahendid', '13:50:00', '15:20:00', '2025-05-30', 'JPLB24', 0),
(176, 'E201', 'svetlana.avdejeva', 'Laboriseadmed ja töövahendid', '08:15:00', '09:45:00', '2025-05-30', 'JPLB24', 0),
(177, 'E201', 'svetlana.avdejeva', 'Laboriseadmed ja töövahendid', '09:55:00', '11:25:00', '2025-05-30', 'JPLB24', 0),
(178, 'E201', 'svetlana.avdejeva', 'Kutseeksam', '09:00:00', '17:00:00', '2025-06-05', 'JPLB22', 1),
(179, 'E201', 'svetlana.avdejeva', 'Kutseeksam', '09:00:00', '17:00:00', '2025-06-06', 'JPLB22', 1),
(180, 'C211', 'viivi.treier', 'Eesti keel teise keelena', '12:10:00', '13:40:00', '2025-05-29', 'JPIT24', 0),
(181, 'C211', 'viivi.treier', 'Eesti keel teise keelena', '13:50:00', '15:20:00', '2025-05-29', 'JPIT24', 0),
(182, 'C211', 'viivi.treier', 'Eesti keel teise keelena', '08:15:00', '09:45:00', '2025-05-30', 'JPIT24', 0),
(183, 'C211', 'viivi.treier', 'Eesti keel teise keelena', '09:55:00', '11:25:00', '2025-05-30', 'JPIT24', 0),
(184, 'C211', 'viivi.treier', 'Eesti keel teise keelena', '12:10:00', '13:40:00', '2025-06-11', 'JPIT24', 0),
(185, 'C211', 'viivi.treier', 'Eesti keel teise keelena', '12:10:00', '13:40:00', '2025-06-12', 'JPIT24', 0),
(186, 'C211', 'viivi.treier', 'Eesti keel teise keelena', '13:50:00', '15:20:00', '2025-06-12', 'JPIT24', 0),
(187, 'C213', 'aleksandr.vainokivi', 'Arvutivõrgud', '08:15:00', '09:45:00', '2025-05-30', 'JPIT23', 0),
(188, 'C213', 'aleksandr.vainokivi', 'Arvutivõrgud', '09:55:00', '11:25:00', '2025-05-30', 'JPIT23', 0),
(189, 'C213', 'aleksandr.vainokivi', 'Arvutivõrgud', '12:10:00', '13:40:00', '2025-05-30', 'JPIT23', 0),
(190, 'C213', 'aleksandr.vainokivi', 'Arvutivõrgud', '13:50:00', '15:20:00', '2025-05-30', 'JPIT23', 0),
(191, 'C213', 'aleksandr.vainokivi', 'Arvutivõrgud', '08:15:00', '09:45:00', '2025-06-03', 'JPIT23', 0),
(192, 'C213', 'aleksandr.vainokivi', 'Arvutivõrgud', '09:55:00', '11:25:00', '2025-06-03', 'JPIT23', 0),
(193, 'C213', 'aleksandr.vainokivi', 'Klientseadmete haldus', '12:10:00', '13:40:00', '2025-06-03', 'JPIT22', 0),
(194, 'C213', 'aleksandr.vainokivi', 'Klientseadmete haldus', '13:50:00', '15:20:00', '2025-06-03', 'JPIT22', 0),
(195, 'C213', 'aleksandr.vainokivi', 'Klientseadmete haldus', '13:50:00', '15:20:00', '2025-06-05', 'JPIT22', 0),
(196, 'C213', 'aleksandr.vainokivi', 'Klientseadmete haldus', '12:10:00', '13:40:00', '2025-06-05', 'JPIT22', 0),
(197, 'C213', 'aleksandr.vainokivi', 'Arvutivõrgud', '08:15:00', '09:45:00', '2025-06-05', 'JPIT23', 0),
(198, 'C213', 'aleksandr.vainokivi', 'Arvutivõrgud', '09:55:00', '11:25:00', '2025-06-05', 'JPIT23', 0);

-- --------------------------------------------------------

--
-- Структура таблицы `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL COMMENT 'User ID',
  `nickname` varchar(255) DEFAULT NULL COMMENT 'User nickname',
  `real_name` varchar(255) DEFAULT NULL COMMENT 'User real name',
  `user_pass` varchar(255) DEFAULT '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4' COMMENT 'User password',
  `prof` varchar(255) DEFAULT NULL COMMENT 'Specialization'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Дамп данных таблицы `users`
--

INSERT INTO `users` (`id`, `nickname`, `real_name`, `user_pass`, `prof`) VALUES
(1, 'vyacheslav.andreev', 'Vyacheslav Andreev', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'aleksander_pulver,nadezda_pahka,tiit_raik,vladislav_mikson,aleksandr_vainokivi,heidi_edela,marina_pavlova,viivi_treier,alevtina_serova,urmas_treier,jaanek_pahka,ilia_bogatyrev,oksana_pavelkovits,tatjana_kippr,anna_torn,eri,jpas,juk1,juk2,laborant'),
(2, 'aleksander.pulver', 'Aleksander Pulver', 'fe2592b42a727e977f055947385b709cc82b16b9a87f88c6abf3900d65d0cdc3', 'aleksander_pulver'),
(3, 'admin', 'Administrator', '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918', 'aleksander_pulver,nadezda_pahka,tiit_raik,vladislav_mikson,aleksandr_vainokivi,heidi_edela,marina_pavlova,viivi_treier,alevtina_serova,urmas_treier,jaanek_pahka,ilia_bogatyrev,oksana_pavelkovits,tatjana_kippr,anna_torn,eri,jpas,juk1,juk2,laborant'),
(4, ' ', ' ', '36a9e7f1c95b82ffb99743e0c5c4ce95d83c9a430aac59f84ef3cbfab6145068', 'aleksander_pulver,nadezda_pahka,tiit_raik,vladislav_mikson,aleksandr_vainokivi,heidi_edela,marina_pavlova,viivi_treier,alevtina_serova,urmas_treier,jaanek_pahka,ilia_bogatyrev,oksana_pavelkovits,tatjana_kippr,anna_torn,eri,jpas,juk1,juk2,laborant'),
(5, 'alevtina.serova', 'Alevtina Serova', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'alevtina_serova'),
(6, 'viivi.treier', 'Viivi Treier', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'viivi_treier'),
(7, 'urmas.treier', 'Urmas Treier', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'urmas_treier'),
(8, 'anna.torn', 'Anna Torn', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'anna_torn'),
(9, 'heidi.edela', 'Heidi Edela', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'heidi_edela'),
(10, 'ilia.bogatyrev', 'Ilia Bogatyrev', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'ilia_bogatyrev'),
(11, 'olga.guskova', 'Olga Guskova', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'eri'),
(12, 'jaanek.pahka', 'Jaanek Pahka', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'jaanek_pahka'),
(13, 'konstantin.malinovski', 'Konstantin Malinovski', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'konstantin_malinovski'),
(14, 'tarvo.seljamae', 'Tarvo Seljamäe', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'tarvo_seljamae'),
(15, 'valeri.bostrov', 'Valeri Bõstrov', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'valeri_bostrov'),
(16, 'nadezda.pahka', 'Nadežda Pahka	', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'nadezda_pahka'),
(17, 'tiit.raik', 'Tiit Raik', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'tiit_raik'),
(18, 'aleksandr.vainokivi', 'Aleksandr Vainokivi', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'aleksandr_vainokivi'),
(19, 'tatjana.kippar', 'Tatjana Kippar', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'tatjana_kippr'),
(20, 'anna.pantelejeva', 'Anna Pantelejeva', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'anna_pantelejeva'),
(21, 'natalia.turilova', 'Natalia Turilova', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'natalia_turilova'),
(22, 'oksana.pavelkovits', 'Oksana Pavelkovitš', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'oksana_pavelkovits'),
(23, 'kulli.veidmann', 'Külli Veidmann', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'eri'),
(24, 'olga.varunina', 'Olga Varunina', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'olga_varunina'),
(25, 'inga.lazarenko', 'Inga Lazarenko', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'inga_lazarenko'),
(26, 'svetlana.avdejeva', 'Svetlana Avdejeva-Stankevitš', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'svetlana_avdejeva'),
(27, 'maarika.rummel', 'Maarika Rümmel', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'maarika_rummel'),
(28, 'irina.leppik', 'Irina Leppik', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'irina_leppik'),
(29, 'marina.pavlova', 'Marina Pavlova', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'marina_pavlova'),
(30, 'vladislav.mikson', 'Vladislav Mikson', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'vladislav_mikson'),
(31, 'juri.melnikov', 'Jüri Melnikov', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'juri_melnikov'),
(32, 'inna.dokutsajeva', 'Inna Dokutšajeva', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'inna_dokutsajeva'),
(33, 'larissa.lavrentjeva', 'Larissa Lavrentjeva', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'larissa_lavrentjeva'),
(34, 'jelena.olikainen', 'Jelena Olikainen', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'jelena_olikainen'),
(35, 'olga.popova', 'Olga Popova', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'olga_popova'),
(36, 'jelena.kuzmina', 'Jelena Kuzmina', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'jelena_kuzmina'),
(37, 'merili.kivimaa', 'Merili Kivimaa', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'merili_kivimaa');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `cabinets`
--
ALTER TABLE `cabinets`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `cabinets`
--
ALTER TABLE `cabinets`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=199;

--
-- AUTO_INCREMENT для таблицы `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'User ID', AUTO_INCREMENT=38;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

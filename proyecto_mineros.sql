-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 15-02-2023 a las 04:54:51
-- Versión del servidor: 10.4.22-MariaDB
-- Versión de PHP: 7.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `proyecto_mineros`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleado`
--

CREATE TABLE `empleado` (
  `CED_EMP` varchar(10) NOT NULL,
  `NOM_EMP` varchar(25) NOT NULL,
  `APE_EMP` varchar(25) NOT NULL,
  `FECHA_NAC` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `empleado`
--

INSERT INTO `empleado` (`CED_EMP`, `NOM_EMP`, `APE_EMP`, `FECHA_NAC`) VALUES
('1804567890', 'JUAN', 'BENITEZ', '1986-01-01'),
('1804567891', 'ADRIAN', 'GALARZA', '1986-01-05'),
('1804567892', 'JOSE', 'PAREDES', '1986-12-01'),
('1804567893', 'ERRECE', 'CASTRO', '1987-02-27'),
('1804567894', 'NACHO', 'GAVILANEZ', '1987-06-25'),
('1804567895', 'BYRON', 'ROMERO', '1987-03-18'),
('1804567896', 'JAZE', 'JACOME', '1988-03-15'),
('1804567897', 'DANI', 'NUÑEZ', '1987-07-07'),
('1804567898', 'FABIOLA', 'SALAZAR', '1988-11-08'),
('1804567899', 'JOSE', 'SANTANA', '1988-09-22');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registro_empleado`
--

CREATE TABLE `registro_empleado` (
  `ID_REGISTRO` int(11) NOT NULL,
  `CED_EMP` varchar(10) NOT NULL,
  `FECHA_ENTRADA` datetime NOT NULL,
  `CASCO` int(1) NOT NULL,
  `CHALECO` int(1) NOT NULL,
  `BOTAS` int(1) NOT NULL,
  `OBSERVACION` varchar(50) NOT NULL,
  `PATH` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `registro_empleado`
--

INSERT INTO `registro_empleado` (`ID_REGISTRO`, `CED_EMP`, `FECHA_ENTRADA`, `CASCO`, `CHALECO`, `BOTAS`, `OBSERVACION`, `PATH`) VALUES
(1, '1804567890', '2023-02-14 01:07:33', 1, 0, 0, '', 'D:\\GitHubProjects\\reconocimiento-mineros-cv-ia\\app_escritorio\\img\\minero.jpg'),
(2, '1804567892', '2023-02-14 20:42:26', 0, 0, 0, '', 'D:\\GitHubProjects\\reconocimiento-mineros-cv-ia\\app_escritorio\\img\\img2.png'),
(3, '1804567891', '2023-02-14 18:34:10', 1, 1, 1, 'ninguna', 'img/2023-02-14-183410656860.jpg'),
(4, '1804567891', '2023-02-14 18:34:10', 1, 1, 1, 'ninguna', 'img/2023-02-14-183410852867.jpg'),
(5, '1804567891', '2023-02-14 18:39:24', 1, 1, 1, 'ninguna', 'img/2023-02-14-183924756636.jpg'),
(6, '1804567891', '2023-02-14 18:47:07', 1, 1, 1, 'ninguna', 'img/2023-02-14-18477303899.jpg');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `empleado`
--
ALTER TABLE `empleado`
  ADD PRIMARY KEY (`CED_EMP`);

--
-- Indices de la tabla `registro_empleado`
--
ALTER TABLE `registro_empleado`
  ADD PRIMARY KEY (`ID_REGISTRO`),
  ADD KEY `EXISTE_EMPLEADO` (`CED_EMP`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `registro_empleado`
--
ALTER TABLE `registro_empleado`
  MODIFY `ID_REGISTRO` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `registro_empleado`
--
ALTER TABLE `registro_empleado`
  ADD CONSTRAINT `EXISTE_EMPLEADO` FOREIGN KEY (`CED_EMP`) REFERENCES `empleado` (`CED_EMP`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

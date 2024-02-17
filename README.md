# diplom

# Система Управления Строительной Компанией

## Обзор

Система предназначена для комплексной автоматизации процессов в строительной компании, охватывая управление документацией, складским учетом, проектами, клиентами, контрагентами, финансами и персоналом. Дополнительно интегрируется с системой уведомлений, управлением ресурсами проекта, а также сервисом аналитики и отчетности для обеспечения эффективного мониторинга и управления ресурсами компании.

## Основные Сервисы

### Сервис Документов

- **Функционал:** Ввод и хранение документов, создание документов по выбранным параметрам и шаблонам.
- **Пользователи:** Бухгалтеры, руководители проектов, менеджеры.

### Сервис Склада

- **Функционал:** Учет материалов, оборудования и транспортных средств на складе, отслеживание доступности и планирование закупок.
- **Пользователи:** Кладовщики, руководители проектов.

### Сервис Клиентов

- **Функционал:** Управление информацией о клиентах, включая проекты, общую сумму проектов.
- **Пользователи:** Менеджеры, высшее руководство.

### Сервис Контрагентов

- **Функционал:** Учет юридической информации о контрагентах.
- **Пользователи:** Бухгалтеры, администраторы системы.

### Сервис Проектов

- **Функционал:** Управление проектами, включая информацию о заказчиках, суммах, участниках проекта и их ролях, финансовом состоянии проектов. Возможно включение Agile доски для управления задачами.
- **Пользователи:** Руководители проектов, высшее руководство.

### Бухгалтерский Сервис

- **Функционал:** Учет финансовых операций, включая поступления, расходы, зарплаты, налоги, создание финансовых отчетов по шаблону.
- **Пользователи:** Бухгалтеры.

### Сервис Сотрудников

- **Функционал:** Создание учетных записей сотрудников, распределение ролей.
- **Пользователи:** Администраторы системы.

## Дополнительные Сервисы

### Система Уведомлений

- **Функционал:** Автоматическая отправка уведомлений о важных событиях через электронную почту, SMS или мобильные уведомления.
- **Пользователи:** Все пользователи системы.

### Сервис Управления Ресурсами Проекта

- **Функционал:** Отслеживание и управление ресурсами проектов, включая материалы, оборудование и транспортные средства.
- **Пользователи:** Руководители проектов, кладовщики.

### Сервис Аналитики и Отчетности

- **Функционал:** Предоставление сводных данных и аналитических дашбордов о ходе выполнения проектов, финансовом состоянии компании, эффективности использования ресурсов.
- **Пользователи:** Аналитики данных, высшее руководство.

## Роли Пользователей

- **Администратор Системы:** Управление сотрудниками, контрагентами, клиентами.
- **Высшее Руководство:** Доступ ко всем сервисам.
- **Бухгалтер:** Доступ к финансовым операциям и отчетам.
- **Руководитель Проектов:** Доступ к управлению проектами и документами.
- **Кладовщик:** Доступ к управлению складом.
- **Менеджер:** Доступ к клиентам, контрагентам и проектам.
- **Сотрудник:** Ограниченный доступ в соответствии с назначенными проектами.
  
![Диаграмма базы данных](https://github.com/IST0VE/diplom/blob/main/out/db/bd.png)
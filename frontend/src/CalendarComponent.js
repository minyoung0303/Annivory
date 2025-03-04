import React from 'react';
import FullCalendar from "@fullcalendar/react";
import dayGridPlugin from '@fullcalendar/daygrid';
import timeGridPlugin from '@fullcalendar/timegrid';
import listPlugin from '@fullcalendar/list';

function CalendarComponent() {
    return (
        <FullCalendar
            plugins={[dayGridPlugin, timeGridPlugin, listPlugin]}
            initialView="dayGridMonth"
            headerToolbar={{
                start: 'prev,next today',
                end: 'dayGridMonth timeGridWeek listMonth'
            }}
            events={[
                { title: '내 생일', start: '2025-03-03' },
                { title: '현호 생일', start: '2025-04-28' }
            ]}
        />
    );
}

export default CalendarComponent;
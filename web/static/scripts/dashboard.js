$(document).ready(function () {
    $('.accept-btn').click(function () {
        const invitationId = $(this).data('invitation-id');
        const invitationType = $(this).data('invitation-type');
        const endpoint = (invitationType === 'team') ? '/update_team_invite' : '/update_game_invite';
        $.ajax({
            url: endpoint,
            method: 'POST',
            data: JSON.stringify({
                invitation_id: invitationId,
                action: 'accept'
            }),
            contentType: 'application/json',
            success: function (response) {
                // handle success response
                $('.invitation-' + invitationId + ' .accept-btn').remove();
                $('.invitation-' + invitationId + ' .decline-btn').remove();
                $('.invitation-' + invitationId + ' .d-flex.justify-content-end').append('<button class="btn btn-secondary px-4" type="button" disabled>Accepted</button>');
            },
            error: function (error) {
                console.error(error);
            }
        });
    });

    $('.decline-btn').click(function () {
        const invitationId = $(this).data('invitation-id');
        const invitationType = $(this).data('invitation-type');
        const endpoint = (invitationType === 'team') ? '/update_team_invite' : '/update_game_invite';
        $.ajax({
            url: endpoint,
            method: 'POST',
            data: JSON.stringify({
                invitation_id: invitationId,
                action: 'decline'
            }),
            contentType: 'application/json',
            success: function (response) {
                // handle success response
                $('.invitation-' + invitationId + ' .accept-btn').remove();
                $('.invitation-' + invitationId + ' .decline-btn').remove();
                $('.invitation-' + invitationId + ' .d-flex.justify-content-end').append('<button class="btn btn-secondary px-4" type="button" disabled>Declined</button>');
            },
            error: function (error) {
                console.error(error);
            }
        });
    });
});
